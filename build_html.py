import base64
import io
import os
from PIL import Image

workspace = r"c:\Users\princ\Downloads\Hall Ticket-html"

def get_b64(filename, max_dim=None):
    path = os.path.join(workspace, filename)
    img = Image.open(path)
    buf = io.BytesIO()
    if max_dim and max(img.size) > max_dim:
        scale = max_dim / max(img.size)
        new_size = (int(img.size[0] * scale), int(img.size[1] * scale))
        img = img.resize(new_size, Image.Resampling.LANCZOS)
    img.save(buf, format="PNG", optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{b64}"

print("Encoding logos...")
msec_b64 = get_b64("mseclogo.png")
anniv_b64 = get_b64("75years.png", 800)
msgi_b64 = get_b64("msgi-logo.png", 500)
print("Logos encoded successfully!")

css_content = """/* ===== MIND SPARK '26 — PREMIUM HALL TICKET ===== */
*{box-sizing:border-box}
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#c1c9dc;font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;padding:24px}
#dc-root,#dc-root>.sc-host{display:flex;align-items:center;justify-content:center}
@media print{
  body{background:transparent !important;padding:0 !important}
  .ticket{box-shadow:none !important}
  .teambox .tfield{background:#FFFFFF !important;border:2px solid #F5B800 !important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .time-box{background:#FFFFFF !important;border:1.5px solid #0B1437 !important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  @page{size:A4 landscape;margin:8mm}
}

.ticket{position:relative;width:880px;height:700px;overflow:hidden;border-radius:18px;color:#0B1437;font-family:'Inter',sans-serif;
  background:
    radial-gradient(900px 420px at 86% 18%, rgba(245,184,0,.08), transparent 62%),
    radial-gradient(760px 440px at 4% 98%, rgba(46,91,191,.09), transparent 60%),
    linear-gradient(176deg,#F8FAFE 0%,#ECF0FA 100%);
  border:2.5px solid #0B1437;
  box-shadow:0 34px 80px -28px rgba(8,16,45,.55),0 0 0 1px rgba(245,184,0,.5),inset 0 0 0 1px rgba(245,184,0,.45)}

.facets{position:absolute;inset:0;z-index:0;pointer-events:none;background:repeating-linear-gradient(118deg,rgba(11,20,55,.016) 0 1px,transparent 1px 30px)}
.wm{position:absolute;right:-24px;bottom:-158px;z-index:0;pointer-events:none;font-family:'Montserrat',sans-serif;font-weight:900;font-size:460px;line-height:.8;color:rgba(11,20,55,.035);transform:rotate(-8deg)}

.inner{position:relative;z-index:5;display:flex;flex-direction:column;height:100%}

/* ---- HEADER ---- */
.hdr{position:relative;height:92px;flex:none;display:flex;align-items:center;justify-content:space-between;padding:0 20px;gap:14px;overflow:hidden;background:linear-gradient(135deg,#0D1C48 0%,#0A1230 55%,#0C183C 100%)}
.hdr::before{content:"";position:absolute;inset:0;background:
  radial-gradient(360px 150px at 15% -12%,rgba(63,111,209,.38),transparent 70%),
  radial-gradient(300px 150px at 93% 125%,rgba(245,184,0,.16),transparent 70%),
  repeating-linear-gradient(124deg,rgba(255,255,255,.03) 0 1px,transparent 1px 24px);pointer-events:none}
.hdr::after{content:"";position:absolute;left:0;right:0;bottom:0;height:3px;background:linear-gradient(90deg,#6f520d,#F5B800 20%,#FFE9A8 50%,#F5B800 80%,#6f520d);z-index:10}

.hdr-card{position:relative;flex:1 1 0;min-width:0;height:70px;display:flex;align-items:center;padding:0 12px;border-radius:12px;background:linear-gradient(135deg,#FFFFFF 0%,#F8FAFE 100%);border:2px solid #F5B800;box-shadow:0 3px 12px rgba(0,0,0,.2),inset 0 0 0 1px rgba(255,255,255,.95);transition:transform .15s ease,box-shadow .15s ease}
.hdr-card:hover{transform:translateY(-1px);box-shadow:0 5px 16px rgba(0,0,0,.26),inset 0 0 0 1px rgba(255,255,255,1),0 0 0 1px rgba(245,184,0,.75)}
.hdr-card.center{justify-content:center}

.logo{display:block;object-fit:contain;filter:drop-shadow(0 1px 2px rgba(11,20,55,.1))}
.logo.msec{width:36px;height:50px;flex:none}
.logo.anniv{max-width:100%;max-height:54px;width:auto;height:auto;object-fit:contain}
.logo.msgi{max-width:100%;max-height:50px;width:auto;height:auto}

.inst-meta{display:flex;flex-direction:column;justify-content:center;min-width:0;margin-left:9px}
.inst-name{font-family:'Montserrat',sans-serif;font-weight:800;font-size:10.5px;line-height:1.15;color:#0B1437;letter-spacing:.25px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.inst-dept{font-family:'Montserrat',sans-serif;font-weight:700;font-size:9.5px;line-height:1.2;color:#1E3A8A;letter-spacing:.45px;margin-top:1px;white-space:nowrap}
.inst-desc{font-family:'Inter',sans-serif;font-weight:500;font-size:8px;line-height:1.25;color:#5D6D96;margin-top:1.5px;letter-spacing:.15px;white-space:nowrap}

/* ---- TITLE ---- */
.title{flex:none;display:flex;justify-content:space-between;align-items:center;gap:18px;padding:14px 32px 8px 32px}
.tl{min-width:0}
.eyebrow-row{display:flex;align-items:center;gap:8px}
.eyebrow{display:inline-block;font-family:'Montserrat',sans-serif;font-weight:800;font-size:10px;letter-spacing:3px;color:#0B1437;padding:3.5px 12px;border-radius:4px;background:linear-gradient(135deg,#FBE7A6,#F5B800 45%,#E0A51C 70%,#FFE9A8);box-shadow:0 2px 6px rgba(197,146,26,.35)}
.eyebrow-sub{font-family:'Montserrat',sans-serif;font-weight:700;font-size:9.5px;letter-spacing:1.5px;color:#2E5BBF;text-transform:uppercase}
.brand{font-family:'Montserrat',sans-serif;font-weight:900;font-size:50px;line-height:.96;letter-spacing:-1px;margin-top:7px;white-space:nowrap}
.brand .mind{color:#0B1437}
.brand .spark{background:linear-gradient(180deg,#5E92F2,#2E5BBF);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.brand .yr{font-size:.44em;vertical-align:super;letter-spacing:0;background:linear-gradient(135deg,#FBE7A6,#F5B800 50%,#C8921A);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.tag{font-family:'Playfair Display',serif;font-style:italic;font-weight:500;font-size:16px;color:#39456F;margin-top:5px}

.tr{flex:none;display:flex;align-items:center}
/* team no. box */
.teambox{flex:none;width:140px;height:86px;border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:7px;background:linear-gradient(160deg,#0E1C49,#0A1230);border:2px solid #F5B800;box-shadow:0 8px 20px -8px rgba(8,16,45,.6),inset 0 0 10px rgba(245,184,0,.12)}
.teambox .tlbl{font-family:'Montserrat',sans-serif;font-weight:800;font-size:11px;letter-spacing:2.8px;color:#F5B800;line-height:1}
.teambox .tfield{width:118px;height:36px;border-radius:9px;background:#FFFFFF;border:2px solid #F5B800;box-shadow:0 2px 6px rgba(0,0,0,.12);display:flex;align-items:center;justify-content:center;text-align:center;outline:none;padding:0;box-sizing:border-box;transition:box-shadow .2s ease,border-color .2s ease}
.teambox .tfield:focus{box-shadow:0 0 0 3px rgba(245,184,0,.35),0 2px 8px rgba(0,0,0,.15)}
.teambox .tval{font-family:'Montserrat',sans-serif;font-weight:800;font-size:16px;color:#0B1437;letter-spacing:1px}

/* ---- INFO STRIP ---- */
.info{flex:none;margin:4px 32px 0 32px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));background:#FFFFFF;border:1.5px solid #0B1437;border-radius:10px;overflow:hidden;box-shadow:0 8px 20px -14px rgba(8,16,45,.4)}
.cell{padding:10px 16px;display:flex;flex-direction:column;justify-content:center}
.cell+.cell{border-left:1.5px solid rgba(11,20,55,.12)}
.ck{display:flex;align-items:center;gap:6px;font-family:'Montserrat',sans-serif;font-weight:800;font-size:9.5px;letter-spacing:1.5px;color:#2E5BBF;text-transform:uppercase}
.ck-dot{width:6px;height:6px;border-radius:50%;background:#F5B800;flex:none;display:inline-block}
.cv{font-family:'Montserrat',sans-serif;font-weight:700;font-size:13px;line-height:1.2;color:#0B1437;margin-top:3.5px;letter-spacing:.1px}
.cv .sup{font-size:.7em;vertical-align:super;font-family:'Montserrat',sans-serif;font-weight:700}
.time-input-wrap{display:flex;align-items:center;gap:8px;margin-top:3.5px}
.time-box{width:96px;height:28px;border-radius:6px;background:#FFFFFF;border:1.5px solid rgba(11,20,55,.3);box-shadow:inset 0 1px 2px rgba(11,20,55,.06);display:flex;align-items:center;justify-content:center;text-align:center;outline:none;padding:0;box-sizing:border-box;transition:border-color .15s ease,box-shadow .15s ease}
.time-box:focus{border-color:#2E5BBF;box-shadow:0 0 0 3px rgba(46,91,191,.15)}
.time-val{font-family:'Montserrat',sans-serif;font-weight:700;font-size:13px;color:#0B1437;letter-spacing:1px}
.time-ampm{font-family:'Montserrat',sans-serif;font-weight:800;font-size:10px;letter-spacing:1px;color:#2E5BBF}

/* ---- CANDIDATE PARTICULARS ---- */
.part{position:relative;flex:1 1 0;min-height:0;margin:12px 32px 0 32px;background:#FFFFFF;border:1.5px solid #0B1437;border-radius:12px;padding:16px 20px 12px 20px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:0 10px 24px -16px rgba(8,16,45,.35)}
.parttab{position:absolute;top:-10px;left:20px;font-family:'Montserrat',sans-serif;font-weight:800;font-size:9.5px;letter-spacing:2.2px;color:#0B1437;padding:3.5px 12px;border-radius:4px;background:linear-gradient(135deg,#FBE7A6,#F5B800 50%,#E0A51C);box-shadow:0 2px 7px rgba(197,146,26,.35)}

/* School Field Box */
.pbox-row{display:flex;align-items:center;background:linear-gradient(135deg,#F8FAFE 0%,#F3F6FD 100%);border:1px solid rgba(11,20,55,.15);border-radius:7px;padding:7px 12px;gap:12px}
.pbox-tag{display:inline-flex;align-items:center;font-family:'Montserrat',sans-serif;font-weight:800;font-size:8.5px;letter-spacing:1.2px;color:#0B1437;background:linear-gradient(135deg,#FDE8A8,#F5B800);padding:2.5px 8px;border-radius:3px;flex:none}
.pbox-lbl{font-family:'Montserrat',sans-serif;font-weight:800;font-size:11px;letter-spacing:.5px;color:#0B1437;white-space:nowrap;flex:none}
.pbox-line{flex:1;min-height:22px;border-bottom:1.5px dashed rgba(11,20,55,.35);display:flex;align-items:center;padding:0 6px;outline:none}

/* 3-Column Student Cards Grid */
.stud-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:4px 0}
.stud-card{background:linear-gradient(135deg,#FFFFFF 0%,#F8FAFD 100%);border:1px solid rgba(11,20,55,.16);border-radius:8px;padding:9px 12px;display:flex;flex-direction:column;gap:7px;box-shadow:0 2px 6px rgba(11,20,55,.04);position:relative}
.stud-head{display:flex;align-items:center;justify-content:space-between}
.stud-badge{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:50%;background:linear-gradient(135deg,#0E1C49,#0A1230);color:#F5B800;font-family:'Montserrat',sans-serif;font-weight:800;font-size:10px;border:1px solid #F5B800}
.stud-role{font-family:'Montserrat',sans-serif;font-weight:800;font-size:9px;letter-spacing:1px;color:#57678E}
.stud-role.lead{color:#2E5BBF}
.stud-field{display:flex;align-items:flex-end;gap:6px}
.stud-flbl{font-family:'Montserrat',sans-serif;font-weight:700;font-size:10px;color:#0B1437;white-space:nowrap;padding-bottom:1px}
.stud-fline{flex:1;min-height:18px;border-bottom:1.5px dashed rgba(11,20,55,.35);display:flex;align-items:center;padding:0 4px;outline:none}
.stud-subrow{display:flex;align-items:flex-end;gap:6px}
.stud-sublbl{font-size:9px;font-weight:600;color:#67769A;white-space:nowrap;padding-bottom:1px}
.stud-subline{flex:1;min-height:16px;border-bottom:1.2px dashed rgba(11,20,55,.28);display:flex;align-items:center;padding:0 4px;outline:none}

/* Editable text styling inside lines */
.field-txt{font-family:'Montserrat',sans-serif;font-weight:700;font-size:11px;color:#0B1437;letter-spacing:.2px;line-height:1;display:inline-block}
.field-txt.sub{font-size:10px;font-weight:600;color:#2E5BBF}

/* Faculty Row */
.fac-row{display:flex;align-items:center;background:linear-gradient(135deg,#F8FAFE 0%,#F3F6FD 100%);border:1px solid rgba(11,20,55,.15);border-radius:7px;padding:7px 12px;gap:14px}
.fac-f1{flex:1.4;display:flex;align-items:center;gap:8px}
.fac-f2{flex:1;display:flex;align-items:center;gap:8px}

/* ---- SIGNATURES ---- */
.sign{flex:none;display:flex;justify-content:space-between;align-items:flex-end;gap:16px;padding:12px 34px 10px 34px}
.sgcol{width:210px;flex:none;display:flex;flex-direction:column;align-items:center}
.sgspace{width:100%;height:44px;display:flex;align-items:flex-end;justify-content:center;padding-bottom:3px}
.sghint{font-family:'Montserrat',sans-serif;font-weight:600;font-size:8.5px;letter-spacing:1px;color:rgba(11,20,55,.25);text-transform:uppercase}
.sgline{width:100%;border-top:1.5px solid #0B1437;margin-bottom:4px}
.sgname{font-family:'Playfair Display',serif;font-weight:600;font-size:14.5px;color:#0B1437}
.sgrole{font-size:9.5px;color:#55618A;text-align:center;margin-top:1px;letter-spacing:.2px}

/* Center Instructions */
.sgcenter{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 12px}
.sgnote{text-align:center}
.sgnote .star{color:#F5B800;font-size:10px;letter-spacing:5px}
.sgnote .nt{font-size:9.5px;color:#55618A;line-height:1.45;margin-top:4px}

/* ---- FOOTER ---- */
.ftr{position:relative;flex:none;height:40px;margin-top:auto;display:flex;align-items:center;justify-content:space-between;padding:0 34px;background:linear-gradient(135deg,#0C183C,#0A1230 60%,#0D1C48);color:#E7ECFA;font-size:12px;font-weight:500}
.ftr::before{content:"";position:absolute;left:0;right:0;top:0;height:3px;background:linear-gradient(90deg,#6f520d,#F5B800 20%,#FFE9A8 50%,#F5B800 80%,#6f520d)}
.fitem{display:flex;align-items:center;gap:8px}
.fk{font-family:'Montserrat',sans-serif;font-weight:800;font-size:8.5px;letter-spacing:1.2px;color:#F5B800;border:1px solid rgba(245,184,0,.5);padding:1.5px 5.5px;border-radius:3px}
"""

full_html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mind Spark '26 Hall Ticket</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Montserrat:wght@600;700;800;900&amp;family=Playfair+Display:ital,wght@0,600;0,700;1,500;1,600&amp;family=Noto+Sans+Devanagari:wght@500;600&amp;display=swap" rel="stylesheet">
<style>
{css_content}
</style>
<script src="./vendor/react.js"></script>
<script src="./vendor/react-dom.js"></script>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Montserrat:wght@600;700;800;900&amp;family=Playfair+Display:ital,wght@0,600;0,700;1,500;1,600&amp;family=Noto+Sans+Devanagari:wght@500;600&amp;display=swap" rel="stylesheet">
<style>
{css_content}
</style>
</helmet>
<div class="ticket">
<div class="facets"></div>
<div class="wm">?</div>
<div class="inner">
<!-- HEADER -->
<div class="hdr">
<div class="hdr-card">
<img class="logo msec" src="{msec_b64}" alt="Meenakshi Sundararajan Engineering College logo">
<div class="inst-meta">
<div class="inst-name">MEENAKSHI SUNDARARAJAN</div>
<div class="inst-dept">ENGINEERING COLLEGE</div>
<div class="inst-desc">Autonomous &middot; Kodambakkam, Chennai</div>
</div>
</div>
<div class="hdr-card center">
<img class="logo anniv" src="{anniv_b64}" alt="75 Years of Inspiring Generations">
</div>
<div class="hdr-card center">
<img class="logo msgi" src="{msgi_b64}" alt="MSGI - Meenakshi Sundararajan Group of Institutions">
</div>
</div>

<!-- TITLE -->
<div class="title">
<div class="tl">
<div class="eyebrow-row">
<div class="eyebrow">HALL TICKET</div>
<div class="eyebrow-sub">OFFICIAL ENTRY ADMIT PASS</div>
</div>
<div class="brand"><span class="mind">MIND</span> <span class="spark">SPARK</span> <span class="yr">&rsquo;26</span></div>
<div class="tag">An Inter-School Quiz Championship</div>
</div>
<div class="tr">
<div class="teambox">
<div class="tlbl">TEAM NO.</div>
<div class="tfield" contenteditable="true" aria-label="Team Number"><span class="tval">001</span></div>
</div>
</div>
</div>

<!-- INFO STRIP -->
<div class="info">
<div class="cell">
<div class="ck"><span class="ck-dot"></span>DATE OF EVENT</div>
<div class="cv">31<span class="sup">st</span> Oct 2026 &middot; Saturday</div>
</div>
<div class="cell">
<div class="ck"><span class="ck-dot"></span>CHAMPIONSHIP VENUE</div>
<div class="cv">MSGI Campus, Kodambakkam, Chennai-24</div>
</div>
<div class="cell">
<div class="ck"><span class="ck-dot"></span>REPORTING TIME</div>
<div class="time-input-wrap">
<div class="time-box" contenteditable="true" aria-label="Reporting Time"><span class="time-val">08:30</span></div>
<span class="time-ampm">AM</span>
</div>
</div>
</div>

<!-- CANDIDATE PARTICULARS (STRUCTURED BOXES) -->
<div class="part">
<div class="parttab">CANDIDATE &amp; SCHOOL PARTICULARS</div>

<!-- School Name Box -->
<div class="pbox-row">
<span class="pbox-tag">INSTITUTION</span>
<span class="pbox-lbl">SCHOOL NAME :</span>
<div class="pbox-line" contenteditable="true"><span class="field-txt">Enter School Name Here</span></div>
</div>

<!-- 3-Column Participant Cards -->
<div class="stud-grid">
<!-- Participant 1 -->
<div class="stud-card">
<div class="stud-head">
<span class="stud-badge">01</span>
<span class="stud-role lead">TEAM LEADER</span>
</div>
<div class="stud-field">
<span class="stud-flbl">Name:</span>
<div class="stud-fline" contenteditable="true"><span class="field-txt">Candidate 1 Name</span></div>
</div>
<div class="stud-subrow">
<span class="stud-sublbl">Class / Sec:</span>
<div class="stud-subline" contenteditable="true"><span class="field-txt sub">XI &mdash; A</span></div>
</div>
</div>

<!-- Participant 2 -->
<div class="stud-card">
<div class="stud-head">
<span class="stud-badge">02</span>
<span class="stud-role">MEMBER 2</span>
</div>
<div class="stud-field">
<span class="stud-flbl">Name:</span>
<div class="stud-fline" contenteditable="true"><span class="field-txt">Candidate 2 Name</span></div>
</div>
<div class="stud-subrow">
<span class="stud-sublbl">Class / Sec:</span>
<div class="stud-subline" contenteditable="true"><span class="field-txt sub">XI &mdash; B</span></div>
</div>
</div>

<!-- Participant 3 -->
<div class="stud-card">
<div class="stud-head">
<span class="stud-badge">03</span>
<span class="stud-role">MEMBER 3</span>
</div>
<div class="stud-field">
<span class="stud-flbl">Name:</span>
<div class="stud-fline" contenteditable="true"><span class="field-txt">Candidate 3 Name</span></div>
</div>
<div class="stud-subrow">
<span class="stud-sublbl">Class / Sec:</span>
<div class="stud-subline" contenteditable="true"><span class="field-txt sub">XII &mdash; A</span></div>
</div>
</div>
</div>

<!-- Faculty Box -->
<div class="fac-row">
<div class="fac-f1">
<span class="pbox-tag">FACULTY</span>
<span class="pbox-lbl">MENTOR NAME :</span>
<div class="pbox-line" contenteditable="true"><span class="field-txt">Teacher / Mentor Name</span></div>
</div>
<div class="fac-f2">
<span class="pbox-lbl">MOBILE NO :</span>
<div class="pbox-line" contenteditable="true"><span class="field-txt">+91 98407 00000</span></div>
</div>
</div>
</div>

<!-- SIGNATURES (PROPER VERTICAL SPACE & STAMP BOX) -->
<div class="sign">
<div class="sgcol">
<div class="sgspace">
<span class="sghint">Signature of Convener</span>
</div>
<div class="sgline"></div>
<div class="sgname">Dr. Joseph George</div>
<div class="sgrole">Program Convener &middot; Head, IIC &amp; Clubs</div>
</div>

<div class="sgcenter">
<div class="sgnote">
<div class="star">&#10022; &#10022; &#10022;</div>
<div class="nt">Produce this Hall Ticket at the registration desk.<br>Entry subject to verification of school credentials.</div>
</div>
</div>

<div class="sgcol">
<div class="sgspace">
<span class="sghint">Signature of Principal</span>
</div>
<div class="sgline"></div>
<div class="sgname">Dr. S.V. Saravanan</div>
<div class="sgrole">Principal, MSEC</div>
</div>
</div>

<!-- FOOTER -->
<div class="ftr">
<div class="fitem"><span class="fk">EMAIL</span> hcc@msec.edu.in</div>
<div class="fitem"><span class="fk">WEB</span> www.msec.edu.in</div>
<div class="fitem"><span class="fk">CALL</span> +91 98407 21869</div>
</div>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":880,"height":700}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
"""

output_path = os.path.join(workspace, "Main.dc.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print("SUCCESS: Main.dc.html written, size:", len(full_html))
