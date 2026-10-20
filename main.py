<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>解鎖世代：運用 AI 進行教師之依附覺察與內在沉澱</title>
    <!-- 引入 html2canvas 套件以支援一鍵轉存圖片 -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        :root {
            --primary: #2d5a40;      /* 靜謐森林綠 */
            --secondary: #7d5a44;    /* 溫暖木質棕 */
            --accent: #e8f0e6;       /* 柔和鼠尾草草綠 */
            --highlight: #d97736;    /* 暖橘點綴 */
            --bg: #fcfbf7;          /* 心靈沉澱米白 */
            --card-bg: #ffffff;
            --text: #2c3e50;
            --light-text: #7f8c8d;
        }

        * { box-sizing: border-box; }

        body {
            font-family: 'PingFang TC', 'Microsoft JhengHei', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 20px;
            line-height: 1.6;
        }

        header {
            text-align: center;
            max-width: 1100px;
            margin: 0 auto 25px auto;
            padding: 30px 20px;
            background: linear-gradient(135deg, #2d5a40, #437a4e);
            color: white;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        }

        header h1 { 
            margin: 0; 
            font-size: 1.9rem; 
            letter-spacing: 1px;
        }

        .nav-tabs {
            display: flex;
            justify-content: center;
            max-width: 1100px;
            margin: 0 auto 20px auto;
            gap: 10px;
            flex-wrap: wrap;
        }

        .tab-btn {
            padding: 12px 18px;
            font-size: 0.95rem;
            font-weight: bold;
            border: none;
            background-color: #e5eae3;
            color: var(--primary);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .tab-btn.active, .tab-btn:hover {
            background-color: var(--primary);
            color: white;
        }

        .tab-content {
            display: none;
            max-width: 1100px;
            margin: 0 auto;
        }

        .tab-content.active { display: block; }

        /* 卡片與網格 */
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 20px;
        }

        .card {
            background: var(--card-bg);
            border-radius: 12px;
            border-left: 6px solid var(--secondary);
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.04);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .card-title {
            font-size: 1.15rem;
            color: var(--primary);
            margin-top: 4px;
            margin-bottom: 8px;
            font-weight: bold;
        }

        .tag {
            display: inline-block;
            background-color: var(--accent);
            color: var(--primary);
            font-size: 0.8rem;
            padding: 3px 8px;
            border-radius: 6px;
            margin-bottom: 6px;
            font-weight: bold;
        }

        .scenario-text {
            font-size: 0.92rem;
            color: var(--text);
            margin-bottom: 12px;
            background: #fbf9f5;
            padding: 10px;
            border-radius: 6px;
            border-left: 3px solid var(--accent);
        }

        /* 閱讀區與語音按鈕 */
        .reading-section {
            background: #ffffff;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 25px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            border-top: 4px solid var(--primary);
        }

        .reading-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
        }

        .reading-article {
            background: #fdfbf7;
            padding: 15px 20px;
            border-radius: 8px;
            margin-top: 10px;
            font-size: 0.94rem;
            color: var(--text);
            line-height: 1.7;
            border-left: 4px solid var(--secondary);
        }

        .btn-audio {
            background-color: var(--primary);
            color: white;
            border: none;
            padding: 6px 14px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.85rem;
            font-weight: bold;
            transition: all 0.2s ease;
        }

        .btn-audio:hover {
            background-color: var(--secondary);
        }

        .prompt-box {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 12px;
            border-radius: 6px;
            font-size: 0.85rem;
            margin-top: 8px;
            position: relative;
            word-break: break-all;
        }

        .btn-copy {
            background-color: var(--secondary);
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.8rem;
            margin-top: 8px;
            float: right;
        }

        .btn-copy:hover { background-color: var(--primary); }

        /* 安頓卡生成頁面 */
        .card-generator {
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            max-width: 650px;
            margin: 0 auto;
        }

        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; font-weight: bold; margin-bottom: 5px; color: var(--primary); }
        .form-control { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 6px; font-size: 0.95rem; }

        .preview-card {
            background: #fdfcf9;
            border: 2px solid var(--secondary);
            padding: 25px;
            border-radius: 12px;
            margin-top: 20px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.03);
        }

        .preview-card h3 { color: var(--primary); margin-top: 0; font-size: 1.4rem; }

        footer { text-align: center; margin-top: 40px; padding: 20px; color: var(--light-text); font-size: 0.85rem; }
    </style>
</head>
<body>

<header>
    <h1>解鎖世代 ✕ 教師之依附覺察與內在沉澱</h1>
</header>

<!-- 加入明確序號 1. 2. 3. 4. 的分頁按鈕區 -->
<div class="nav-tabs">
    <button class="tab-btn" onclick="switchTab('tab0')">1. 📚 《家庭教育法》10 大範疇</button>
    <button class="tab-btn active" onclick="switchTab('tab1')">2. 🌱 焦慮情境與情緒冰山覺察</button>
    <button class="tab-btn" onclick="switchTab('tab2')">3. 💬 AI 引導 Prompt</button>
    <button class="tab-btn" onclick="switchTab('tab3')">4. 🃏 產出 G2 內在安頓卡（去蕪存菁）</button>
</div>

<!-- 分頁 0：10大範疇簡介 -->
<div id="tab0" class="tab-content">
    <div style="background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
        <h3 style="color: var(--primary); margin: 0 0 8px 0;">家庭教育 10 大範疇與定義概覽</h3>
        <p style="margin: 0; color: var(--light-text);">家庭教育不限於親職教育。本專案以「倫理教育」與「情緒教育」為核心，協助教師觀照自身（G2）世代樞紐位置：</p>
    </div>

    <div class="grid-container">
        <div class="card" style="border-left-color: #2d5a40;">
            <div>
                <div class="card-title">1. 親職教育</div>
                <p style="margin: 0; font-size: 0.93rem;">增進父母或監護人了解應盡職責與教養子女之知能。</p>
            </div>
        </div>
        <div class="card" style="border-left-color: #2d5a40;">
            <div>
                <div class="card-title">2. 子職教育</div>
                <p style="margin: 0; font-size: 0.93rem;">增進子女了解應盡本分之知能。</p>
            </div>
        </div>
        <div class="card" style="border-left-color: #2d5a40;">
            <div>
                <div class="card-title">3. 性別教育</div>
                <p style="margin: 0; font-size: 0.93rem;">增進性別交往與互動之知能。</p>
            </div>
        </div>
        <div class="card" style="border-left-color: #2d5a40;">
            <div>
                <div class="card-title">4. 婚姻教育</div>
                <p style="margin: 0; font-size: 0.93rem;">增進夫妻溝通、經營與相處之知能。</p>
            </div>
        </div>
        <div class="card" style="border-left-color: #2d5a40;">
            <div>
                <div class="card-title">5. 失親教育</div>
                <p style="margin: 0; font-size: 0.93rem;">協助面對失去家庭成員、調適心理與生活的教育活動。</p>
            </div>
        </div>
        <div class="card" style="border-left-color: var(--highlight); background-color: #fffdfa;">
            <div>
                <span class="tag" style="background-color: #fde8d7; color: var(--highlight);">★ 本專案核心</span>
                <div class="card-title">6. 倫理教育</div>
                <p style="margin: 0; font-size: 0.93rem;">增進家族成員倫理關係與互動的教育活動（代間傳遞與世代承載）。</p>
            </div>
        </div>
        <div class="card" style="border-left-color: #2d5a40;">
            <div>
                <div class="card-title">7. 資源管理教育</div>
                <p style="margin: 0; font-size: 0.93rem;">增進家庭時間、金錢與各類資源分配及運用之知能。</p>
            </div>
        </div>
        <div class="card" style="border-left-color: #2d5a40;">
            <div>
                <div class="card-title">8. 多元文化教育</div>
                <p style="margin: 0; font-size: 0.93rem;">增進對不同文化背景家庭與族群理解包容之知能。</p>
            </div>
        </div>
        <div class="card" style="border-left-color: var(--highlight); background-color: #fffdfa;">
            <div>
                <span class="tag" style="background-color: #fde8d7; color: var(--highlight);">★ 本專案核心</span>
                <div class="card-title">9. 情緒教育</div>
                <p style="margin: 0; font-size: 0.93rem;">增進個人情緒覺察、表達與自我調節之知能（內在冰山與安頓沉澱）。</p>
            </div>
        </div>
        <div class="card" style="border-left-color: #2d5a40;">
            <div>
                <div class="card-title">10. 人口教育</div>
                <p style="margin: 0; font-size: 0.93rem;">增進對人口結構改變、少子化或高齡化等現象認知之知能。</p>
            </div>
        </div>
    </div>
</div>

<!-- 分頁 1：焦慮情境切入與主題短文閱讀 -->
<div id="tab1" class="tab-content active">
    <!-- 主題短文閱讀區 1 -->
    <div class="reading-section">
        <div class="reading-header">
            <div>
                <h3 style="color: var(--primary); margin: 0;">📖 沉澱閱讀（一）：看見世代的鎖鏈，從 G1 的歷史找到內在安頓</h3>
                <p style="color: var(--light-text); font-size: 0.88rem; margin: 4px 0 0 0;">聚焦代間依附傳遞與情緒覺察（對應依附與情緒主題）：</p>
            </div>
            <div>
                <button class="btn-audio" onclick="playAudio('article1', this)">🔊 語音導讀</button>
                <button class="btn-audio" style="background-color: #7d5a44;" onclick="stopAudio()">⏹ 停止朗讀</button>
            </div>
        </div>
        <div class="reading-article" id="article1">
            根據心理學家 Bowlby 與 Mary Main 的研究，人在原生家庭所形成的依附關係，有 70% 至 80% 會在世代間被無意識地複製與傳遞。作為國小教師（G2 中間世代），我們常在面對學生失控或家長質疑的瞬間，觸發內在未被滿足的情感需求。當我們感到憤怒或想防衛時，那往往不是對眼前的事件發火，而是觸動了童年成長經驗中「害怕失控」或「渴望被肯定」的記憶。
            <br><br>
            改變他人之前，必須先理解自己的童年。試著探究 G1 父母當時的求學背景、家庭排行與生存壓力——看見父母的侷限後，我們便不再責怪自己或父母，而是能以理智與溫柔看見世代的傳遞。透過這場沉澱，我們可以自主決定：哪些不好的互動模式該在我們這世代「斬斷（去蕪）」，哪些正向的力量值得被「保留（存菁）」。
        </div>
    </div>

    <div style="background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
        <h3 style="color: var(--primary); margin: 0 0 8px 0;">忙碌的教學與家庭生活中，辛苦你了。</h3>
        <p style="margin: 0; color: var(--light-text);">請點選最貼近你當前臨場狀態的情境，作為開啟 G1-G2 依附覺察與內在沉澱的起點：</p>
    </div>

    <div class="grid-container">
        <div class="card">
            <div>
                <span class="tag">親師溝通 ✕ 討好防衛</span>
                <div class="card-title">📱 情境 A：「老師，是不是你在針對我家小孩？」</div>
                <div class="scenario-text">
                    <strong>臨場對話：</strong>面對家長語氣不善的質疑，心中瞬間緊繃，產生強烈的被否定感與焦慮，急著想解釋或委屈忍讓。
                </div>
            </div>
            <div class="prompt-box">
                <span>面對家長質疑時我感到強烈的焦慮與委屈，請陪我運用情緒冰山與依附理論梳理我內在討好/防禦的聲音。</span>
                <button class="btn-copy" onclick="copyText(this)">複製引導詞</button>
            </div>
        </div>

        <div class="card">
            <div>
                <span class="tag">師生互動 ✕ 失控情緒</span>
                <div class="card-title">🏫 情境 B：課堂上學生突如其來的失控與挑釁</div>
                <div class="scenario-text">
                    <strong>臨場對話：</strong>「我就是不要寫做不行嗎！」面對學生情緒失控，多次勸導無效後，心中一股無名火升起，無力感蔓延。
                </div>
            </div>
            <div class="prompt-box">
                <span>面對學生的失控反應時我發現自己很容易被激怒，請引導我看見內在冰山底層的情感需求與童年被要求的記憶。</span>
                <button class="btn-copy" onclick="copyText(this)">複製引導詞</button>
            </div>
        </div>

        <div class="card">
            <div>
                <span class="tag">代間互動 ✕ 權力干預</span>
                <div class="card-title">🏠 情境 C：「你這樣教小孩/當老師不行啦！」</div>
                <div class="scenario-text">
                    <strong>臨場對話：</strong>回到家或聚會時，G1 原生家庭長輩指手畫腳下指令，心中立刻升起一股熟悉的煩躁與抗拒。
                </div>
            </div>
            <div class="prompt-box">
                <span>面對 G1 長輩的教養干預我常感到煩躁與被否定，請陪我探究 G1 父母的童年背景，幫我建立心理界線。</span>
                <button class="btn-copy" onclick="copyText(this)">複製引導詞</button>
            </div>
        </div>

        <div class="card">
            <div>
                <span class="tag">G2 樞紐 ✕ 能量耗竭</span>
                <div class="card-title">⚖️ 情境 D：夾在照顧長輩與教學之間的窒息感</div>
                <div class="scenario-text">
                    <strong>臨場對話：</strong>白天安撫幾十個學生與家長，下班還要關心高齡父母（G1）的身體，感覺自己像個陀螺，完全沒有自己。
                </div>
            </div>
            <div class="prompt-box">
                <span>我覺得自己夾在照顧長輩與教學責任之間被抽乾，請陪我進行一場『去蕪存菁』的沉澱對話，協助我找回自我。</span>
                <button class="btn-copy" onclick="copyText(this)">複製引導詞</button>
            </div>
        </div>

        <div class="card">
            <div>
                <span class="tag">防衛機制 ✕ 超理智隔離</span>
                <div class="card-title">🤐 情境 E：「反正按照規定來就好，不用談感情」</div>
                <div class="scenario-text">
                    <strong>臨場對話：</strong>遇到高壓衝突時，習慣立刻切斷情緒，用冷漠、嚴厲的規則武裝自己，事後卻感到無比孤立與疲憊。
                </div>
            </div>
            <div class="prompt-box">
                <span>衝突時我常習慣切斷感覺用超理智防衛，請陪我看見我內在害怕受傷的脆弱，建立健康的溫和溝通。</span>
                <button class="btn-copy" onclick="copyText(this)">複製引導詞</button>
            </div>
        </div>

        <div class="card">
            <div>
                <span class="tag">自我批判 ✕ 完美主義</span>
                <div class="card-title">🥺 情境 F：「是不是我不夠好，才會處理不好事情？」</div>
                <div class="scenario-text">
                    <strong>臨場對話：</strong>只要有一個家長不滿意或學生沒學好，就深深陷入自責黑洞，不斷批判自己不是個合格的好老師。
                </div>
            </div>
            <div class="prompt-box">
                <span>我常陷入完美主義與自我批判的黑洞中，請陪我尋找『自己好，別人也好』的安全依附自尊，安頓我自己。</span>
                <button class="btn-copy" onclick="copyText(this)">複製引導詞</button>
            </div>
        </div>
    </div>
</div>

<!-- 分頁 2：AI 引導 Prompt 庫與主題短文閱讀 -->
<div id="tab2" class="tab-content">
    <!-- 主題短文閱讀區 2 -->
    <div class="reading-section">
        <div class="reading-header">
            <div>
                <h3 style="color: var(--primary); margin: 0;">📖 沉澱閱讀（二）：衝突是理解的開始，從尖銳開場到雙向溝通</h3>
                <p style="color: var(--light-text); font-size: 0.88rem; margin: 4px 0 0 0;">聚焦溝通轉化與衝突應對（對應衝突與溝通主題）：</p>
            </div>
            <div>
                <button class="btn-audio" onclick="playAudio('article2', this)">🔊 語音導讀</button>
                <button class="btn-audio" style="background-color: #7d5a44;" onclick="stopAudio()">⏹ 停止朗讀</button>
            </div>
        </div>
        <div class="reading-article" id="article2">
            在親師對話或師生互動中，衝突往往源於雙方「視角不同」與「期待未被看見」。根據 David H. Olson 的衝突模式，爭執發生的前三分鐘，幾乎就能預測該次衝突的結果。當我們習慣用帶有指責或防禦的「尖銳開場」對話時，往往會激起對方的生氣與反彈；相反地，若能採取「溫和開場（Soft Startup）」——抱怨事情但不攻擊個人，就能顯著提升解決問題的可能性。
            <br><br>
            當衝突發生、心跳每分鐘超過一百下時，身體正處於高壓狀態，難以理性思考。此時最需要暫停 20 分鐘進行深呼吸與平復。請記住，溝通不只是告知想法，更需要「澄清立場與表達需求」。將籠統的抱怨轉化為具體的需求表達（描述客觀事實 + 表達感受 + 提出期待），並透過日常的正念與感謝積累「關係存款」，我們就能在維繫關係的前提下，達到真正的共識與和解。
        </div>
    </div>

    <div style="background: white; padding: 25px; border-radius: 12px; max-width: 850px; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.04);">
        <h3 style="color: var(--primary); margin-top: 0;">💬 複製 AI 溫柔心理導引 System Prompt 庫</h3>
        <p style="color: var(--light-text); font-size: 0.95rem;">您可以選擇複製【核心一對一導引卡】，或複製下方的【專屬功能深化 Prompt】貼入 Gemini 進行演練：</p>
        
        <!-- 核心 1 對 1 主指令 -->
        <div style="margin-bottom: 25px;">
            <span class="tag" style="background: var(--primary); color: white;">★ 核心一對一沉澱 System Prompt</span>
            <div class="prompt-box" style="white-space: pre-wrap; font-family: monospace; line-height: 1.5; font-size: 0.88rem;">請扮演一位具備家庭系統與依附理論知能的「溫柔心理引導者」。我是一位國小教師（G2中間世代），請陪伴我進行 15 分鐘的原生家庭（G1）依附覺察與內在沉澱。

【核心引導原則】：
1. 嚴格控管每次回覆長度在 3 句話以內，保持客觀、溫柔、無評價與高度接納。
2. 每次僅提出 1 個開放式問題，陪伴我逐步經歷以下四大步驟：
   - Step 1【看見情緒冰山】：無條件接納當前焦慮，引導看見喜怒哀樂背後未被滿足的情感需求（如：接納、尊重、安全感）。
   - Step 2【回顧童年與探究父母（G1）】：引導探究 G1 父母長大的時代背景、求學經歷與侷限，理解「不是責怪自己或父母，而是看見世代間依附風格的複製與傳遞（70-80%）」。
   - Step 3【去蕪存菁】：引導梳理「你想斬斷的不好互動模式（去蕪）」與「你想保留/建立的好模式（存菁）」。
   - Step 4【內在安頓】：協助我產出一句專屬的 G2 內在安頓肯定句。

3. 請先用一句溫暖的話問候我，並邀請我分享今天最想被安頓的情緒或溝通困境。</div>
            <button class="btn-copy" style="float: none; margin-top: 10px; background: var(--primary);" onclick="copyText(this)">📋 一鍵複製完整 System Prompt</button>
        </div>

        <hr style="border: 0.5px solid var(--accent); margin: 25px 0;">

        <!-- 專屬功能 Prompt -->
        <h4 style="color: var(--primary); margin-bottom: 15px;">🔍 講義精華：專屬功能演練 Prompt 模組</h4>
        
        <div class="grid-container" style="grid-template-columns: 1fr;">
            <!-- 功能 1 -->
            <div class="card" style="border-left-color: var(--secondary);">
                <div>
                    <span class="tag">探究父母童年 ✕ 去蕪存菁</span>
                    <div class="card-title">1. G1 父母童年歷史與換位思考 Prompt</div>
                    <p style="font-size: 0.88rem; margin-bottom: 8px;">引導教師梳理 G1 父母的排行、求學經歷與時代限制，看見「父母也是被複製的童年」。</p>
                </div>
                <div class="prompt-box">
                    <span>請陪伴我探究我父母（G1高齡世代）成長的時代背景、家庭排行與當時的生存壓力。請用 3 個開放式提問，協助我看見父母管教方式背後的無奈與侷限，幫助我卸下心結，完成去蕪存菁。</span>
                    <button class="btn-copy" onclick="copyText(this)">複製 Prompt</button>
                </div>
            </div>

            <!-- 功能 2 -->
            <div class="card" style="border-left-color: var(--secondary);">
                <div>
                    <span class="tag">衝突溝通 ✕ 溫和開場</span>
                    <div class="card-title">2. 爭執前 3 分鐘「溫和開場（Soft Startup）」轉化 Prompt</div>
                    <p style="font-size: 0.88rem; margin-bottom: 8px;">把帶有批判、尖銳的對話（如家長/學生衝突），改寫為「抱怨但不攻擊」的溫和開場句。推演爭執前三分鐘的關鍵溝通。</p>
                </div>
                <div class="prompt-box">
                    <span>當我想向【家長/學生/G1長輩】表達不滿時，我常不小心變得尖銳防衛。請引導我將原本想講的生氣話，演練轉化為包含『描述客觀事實 + 表達自身感受 + 提出具體期待』的 3 分鐘溫和開場句。</span>
                    <button class="btn-copy" onclick="copyText(this)">複製 Prompt</button>
                </div>
            </div>

            <!-- 功能 3 -->
            <div class="card" style="border-left-color: var(--secondary);">
                <div>
                    <span class="tag">具體需求 ✕ 告別抱怨</span>
                    <div class="card-title">3. 具體化「情感需求與清晰期待」引導 Prompt</div>
                    <p style="font-size: 0.88rem; margin-bottom: 8px;">協助教師停下籠統的抱怨，將心中的焦慮具體化為能讓對方理解的「情感需求」。</p>
                </div>
                <div class="prompt-box">
                    <span>我發現自己最近對【教學/親師關係】有很多籠統的抱怨。請引導我透過薩提爾冰山，看見我底層最渴望獲得的『被尊重、被理解或安全感』需求，並教我如何清晰表達出來。</span>
                    <button class="btn-copy" onclick="copyText(this)">複製 Prompt</button>
                </div>
            </div>

            <!-- 功能 4 -->
            <div class="card" style="border-left-color: var(--secondary);">
                <div>
                    <span class="tag">正念安頓 ✕ 關係存款</span>
                    <div class="card-title">4. 3 分鐘正念感謝冥想與內在賦能 Prompt</div>
                    <p style="font-size: 0.88rem; margin-bottom: 8px;">引導教師進行深呼吸與細數感謝，快速平復每分鐘超過百下的緊張心率，累積關係存款。推演衝突後的自我調適。</p>
                </div>
                <div class="prompt-box">
                    <span>我現在感到非常疲憊與焦慮，請帶領我進行一段 3 分鐘的正念呼吸與感謝冥想，引導我將注意力帶回當下，找回安心感與感謝的力量。</span>
                    <button class="btn-copy" onclick="copyText(this)">複製 Prompt</button>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- 分頁 3：生成安頓卡 -->
<div id="tab3" class="tab-content">
    <div class="card-generator">
        <h3 style="color: var(--primary); text-align: center; margin-top: 0;">🃏 製作專屬「G2 內在安頓與去蕪存菁卡」</h3>
        <p style="text-align: center; color: var(--light-text); font-size: 0.9rem; margin-bottom: 20px;">根據對話結果，填入屬於您的去蕪存菁抉擇，生成可隨身儲存的安頓圖卡：</p>
        
        <div class="form-group">
            <label>給自己的 G2 內在安頓肯定句：</label>
            <input type="text" id="affirmationInput" class="form-control" value="我是穩定的樞紐，看見世代傳遞後，我選擇帶著理解與界線溫柔前行。">
        </div>

        <div class="form-group">
            <label>✂️ 想斬斷/放下的舊模式（去蕪）：</label>
            <input type="text" id="removeInput" class="form-control" value="過度承擔他人情緒、尖銳式溝通開場、複製 G1 的權威防衛">
        </div>

        <div class="form-group">
            <label>🌱 想保留/建立的新力量（存菁）：</label>
            <input type="text" id="keepInput" class="form-control" value="溫和開場與傾聽、建立心理健康界線、積累關係存款">
        </div>

        <button class="btn-copy" id="downloadBtn" style="width: 100%; padding: 12px; font-size: 1rem; float: none; background: var(--primary);" onclick="generateAndDownloadCard()">✨ 生成並下載個人安頓卡圖片 (PNG)</button>

        <div class="preview-card" id="cardPreview">
            <h3>👑 《解鎖世代》G2 內在安頓卡</h3>
            <p id="cardAffirmation" style="font-size: 1.1rem; color: var(--secondary); font-weight: bold; margin: 15px 0;">"我是穩定的樞紐，看見世代傳遞後，我選擇帶著理解與界線溫柔前行。"</p>
            <hr style="border: 0.5px solid var(--accent); margin: 15px 0;">
            <p style="text-align: left; margin: 8px 0;"><strong>✂️ 去蕪 (斬斷與放下)：</strong> <span id="cardRemove">過度承擔他人情緒、尖銳式溝通開場、複製 G1 的權威防衛</span></p>
            <p style="text-align: left; margin: 8px 0;"><strong>🌱 存菁 (保留與建立)：</strong> <span id="cardKeep">溫和開場與傾聽、建立心理健康界線、積累關係存款</span></p>
        </div>
    </div>
</div>

<footer>
    <p>設計者：國北教大 學習科技與媒體研究團隊 ✕ 家庭教育專業推廣專案</p>
</footer>

<script>
    function switchTab(tabId) {
        // 切換 Tab 時自動停止正在播放的語音
        stopAudio();

        document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
        
        event.target.classList.add('active');
        document.getElementById(tabId).classList.add('active');
    }

    function copyText(button) {
        const textToCopy = button.previousElementSibling ? button.previousElementSibling.innerText : button.parentElement.querySelector('div').innerText;
        navigator.clipboard.writeText(textToCopy).then(() => {
            const originalText = button.innerText;
            button.innerText = '已複製！';
            button.style.backgroundColor = '#27ae60';
            setTimeout(() => {
                button.innerText = originalText;
                button.style.backgroundColor = '#7d5a44';
            }, 1500);
        });
    }

    // 語音導讀引擎（Web Speech API）
    function playAudio(elementId, button) {
        // 停止之前的播放
        window.speechSynthesis.cancel();

        const text = document.getElementById(elementId).innerText;
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'zh-TW';
        utterance.rate = 0.95; // 稍微放慢速度，營造沈靜舒緩感

        utterance.onstart = () => {
            button.innerText = '🔊 正在導讀中...';
            button.style.backgroundColor = '#27ae60';
        };

        utterance.onend = () => {
            button.innerText = '🔊 語音導讀';
            button.style.backgroundColor = '#2d5a40';
        };

        window.speechSynthesis.speak(utterance);
    }

    function stopAudio() {
        window.speechSynthesis.cancel();
        document.querySelectorAll('.btn-audio').forEach(btn => {
            if (btn.innerText.includes('正在導讀')) {
                btn.innerText = '🔊 語音導讀';
                btn.style.backgroundColor = '#2d5a40';
            }
        });
    }

    // 自動更新文字並下載 PNG 圖卡
    function generateAndDownloadCard() {
        const btn = document.getElementById('downloadBtn');
        btn.innerText = '⏳ 正在繪製圖片並下載中...';
        btn.style.backgroundColor = '#7d5a44';

        // 1. 更新預覽區文字
        document.getElementById('cardAffirmation').innerText = '"' + document.getElementById('affirmationInput').value + '"';
        document.getElementById('cardRemove').innerText = document.getElementById('removeInput').value;
        document.getElementById('cardKeep').innerText = document.getElementById('keepInput').value;

        // 2. 將預覽卡片轉為 Canvas 圖片並觸發下載
        const cardElement = document.getElementById('cardPreview');
        html2canvas(cardElement, {
            scale: 2, // 提高圖片解析度
            backgroundColor: '#fdfcf9'
        }).then(canvas => {
            const link = document.createElement('a');
            link.download = 'G2_內在安頓卡.png';
            link.href = canvas.toDataURL('image/png');
            link.click();

            btn.innerText = '✅ 已成功下載圖片！';
            btn.style.backgroundColor = '#27ae60';
            setTimeout(() => {
                btn.innerText = '✨ 生成並下載個人安頓卡圖片 (PNG)';
                btn.style.backgroundColor = '#2d5a40';
            }, 2000);
        }).catch(err => {
            console.error('下載失敗:', err);
            btn.innerText = '✨ 已更新內容 (若未自動下載可直接對卡片截圖)';
            setTimeout(() => {
                btn.innerText = '✨ 生成並下載個人安頓卡圖片 (PNG)';
                btn.style.backgroundColor = '#2d5a40';
            }, 2500);
        });
    }
</script>

</body>
</html>
