/**
 * Katalyst — append coverage rows from the daily tracker email.
 *
 * Lives inside the coverage workbook (Extensions › Apps Script), so it runs in
 * Nikhila's own Google account. Nothing to host, nothing to maintain, and if it
 * ever stops working the email still arrives and someone pastes by hand.
 *
 * SETUP, once:
 *   1. Open Katalyst_PR_Coverage_WORKING → Extensions → Apps Script.
 *   2. Paste this file in, Save.
 *   3. Run `appendCoverageFromEmail` once by hand and approve the permission
 *      prompt (it needs Gmail read + Sheets write on this file).
 *   4. Triggers (clock icon) → Add trigger → appendCoverageFromEmail →
 *      Time-driven → Day timer → 12:00–13:00. That is after the tracker's
 *      11:00 run.
 *
 * It reads the tab-separated block the tracker puts between its markers,
 * skips anything whose Link already exists, and appends the rest.
 */

var SHEET_NAME   = 'ALL_COVERAGE';
var LINK_COLUMN  = 8;    // H — Date, Client, Group, Publication, Tier, Reach, Topic, Link
var COLUMN_COUNT = 14;
var START_MARK   = '---KATALYST-ROWS-START---';
var END_MARK     = '---KATALYST-ROWS-END---';
var GMAIL_QUERY  = 'subject:"PR Coverage" newer_than:2d';
var DONE_LABEL   = 'katalyst-logged';

function appendCoverageFromEmail() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);
  if (!sheet) throw new Error('No tab named ' + SHEET_NAME);

  var label   = getOrCreateLabel_(DONE_LABEL);
  var threads = GmailApp.search(GMAIL_QUERY + ' -label:' + DONE_LABEL);
  if (!threads.length) { log_('No unprocessed tracker email found.'); return; }

  var existing = existingLinks_(sheet);
  var toAppend = [];
  var seen     = {};

  threads.forEach(function (thread) {
    thread.getMessages().forEach(function (msg) {
      parseRows_(msg.getPlainBody()).forEach(function (row) {
        var key = normaliseLink_(row[LINK_COLUMN - 1]);
        // A row with no usable link still gets logged — print coverage has none —
        // but it cannot be deduplicated, so it is left for a human to check.
        if (key) {
          if (existing[key] || seen[key]) return;
          seen[key] = true;
        }
        toAppend.push(row);
      });
    });
    thread.addLabel(label);
  });

  if (!toAppend.length) { log_('Nothing new to append.'); return; }

  sheet.getRange(sheet.getLastRow() + 1, 1, toAppend.length, COLUMN_COUNT)
       .setValues(toAppend);
  log_('Appended ' + toAppend.length + ' row(s).');
}

/** Pull tab-separated rows from between the tracker's markers. */
function parseRows_(body) {
  var out = [];
  if (!body) return out;
  var start = body.indexOf(START_MARK);
  var end   = body.indexOf(END_MARK);
  if (start === -1 || end === -1 || end < start) return out;

  body.substring(start + START_MARK.length, end)
      .split(/\r?\n/)
      .forEach(function (line) {
        if (!line.trim()) return;
        var cells = line.split('\t');
        // Ignore anything that is not a full row rather than appending a short
        // one — a short row shifts every column after it and is worse than a miss.
        if (cells.length < COLUMN_COUNT) return;
        out.push(cells.slice(0, COLUMN_COUNT).map(function (c) { return c.trim(); }));
      });
  return out;
}

/** Same normalisation the tracker uses, so both sides agree on what a duplicate is. */
function normaliseLink_(url) {
  if (!url) return '';
  var u = String(url).trim();
  if (u.indexOf('http') !== 0) return '';
  var m = u.match(/[?&]q=([^&]+)/);
  if (u.indexOf('google.com/url') !== -1 && m) u = decodeURIComponent(m[1]);
  return u.replace(/^https?:\/\//, '')
          .replace(/^www\./, '')
          .replace(/\/amp\//, '/')
          .split('?')[0]
          .split('#')[0]
          .replace(/\/$/, '')
          .toLowerCase();
}

function existingLinks_(sheet) {
  var map  = {};
  var last = sheet.getLastRow();
  if (last < 2) return map;
  sheet.getRange(2, LINK_COLUMN, last - 1, 1).getValues().forEach(function (r) {
    var k = normaliseLink_(r[0]);
    if (k) map[k] = true;
  });
  return map;
}

function getOrCreateLabel_(name) {
  return GmailApp.getUserLabelByName(name) || GmailApp.createLabel(name);
}

function log_(msg) {
  Logger.log(msg);
}
