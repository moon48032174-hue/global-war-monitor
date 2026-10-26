[index.html](https://github.com/user-attachments/files/33957381/index.html)
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>세계 전쟁 및 분쟁 실시간 감시 대시보드 (Global Conflict Monitor)</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@300;400;600;700;800&display=swap');
        body {
            font-family: 'Pretendard', sans-serif;
            background-color: #0b0f19;
            color: #f3f4f6;
        }
        .glass-panel {
            background: rgba(17, 24, 39, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .glow-red {
            box-shadow: 0 0 15px rgba(239, 68, 68, 0.3);
        }
        .pulse-dot {
            animation: pulse 1.5s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.4; transform: scale(1.2); }
        }
    </style>
</head>
<body class="min-h-screen flex flex-col">

    <!-- 상단 헤더 -->
    <header class="glass-panel sticky top-0 z-50 border-b border-gray-800 px-6 py-4 flex flex-wrap justify-between items-center">
        <div class="flex items-center space-x-3">
            <div class="relative flex items-center justify-center">
                <span class="w-3.5 h-3.5 bg-red-500 rounded-full pulse-dot"></span>
                <span class="absolute w-6 h-6 bg-red-500/30 rounded-full"></span>
            </div>
            <h1 class="text-xl font-extrabold tracking-wider bg-clip-text text-transparent bg-gradient-to-r from-red-500 via-amber-400 to-cyan-400">
                GLOBAL WAR & CONFLICT MONITOR
            </h1>
            <span class="text-xs px-2 py-0.5 rounded border border-red-500/40 text-red-400 font-mono">LIVE INTELLIGENCE</span>
        </div>
        
        <div class="flex items-center space-x-4 mt-2 sm:mt-0">
            <div id="backend-status" class="flex items-center space-x-2 text-xs text-gray-400 bg-gray-800/60 px-3 py-1.5 rounded-full border border-gray-700">
                <span class="w-2 h-2 rounded-full bg-amber-500" id="status-indicator"></span>
                <span id="status-text">백엔드 연결 대기중</span>
            </div>
            <button onclick="triggerBackendSync()" class="flex items-center space-x-1 text-xs bg-red-600/80 hover:bg-red-600 text-white px-3 py-1.5 rounded-lg transition font-medium glow-red">
                <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                <span>실시간 수집 연동</span>
            </button>
        </div>
    </header>

    <!-- 메인 콘텐츠 영역 -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 md:p-6 space-y-6">

        <!-- 1. 최상단: 세계 종합 위기 게이지 & 핵심 지표 -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            
            <!-- 게이지 카드 -->
            <div class="glass-panel p-6 rounded-2xl flex flex-col items-center justify-center relative overflow-hidden">
                <div class="absolute -right-10 -bottom-10 w-40 h-40 bg-red-500/10 rounded-full blur-3xl"></div>
                <h2 class="text-sm font-semibold text-gray-400 uppercase tracking-widest mb-2 flex items-center gap-2">
                    <i data-lucide="shield-alert" class="w-4 h-4 text-red-500"></i> 세계 분쟁 위기 진행률 (Global War Index)
                </h2>
                
                <div class="relative flex items-center justify-center my-4">
                    <!-- SVG 게이지 차트 -->
                    <svg class="w-48 h-48 transform -rotate-90">
                        <circle cx="96" cy="96" r="80" stroke="#1f2937" stroke-width="14" fill="transparent" />
                        <circle id="gauge-circle" cx="96" cy="96" r="80" stroke="#ef4444" stroke-width="14" fill="transparent" 
                                stroke-dasharray="502.6" stroke-dashoffset="175" stroke-linecap="round" class="transition-all duration-1000" />
                    </svg>
                    <div class="absolute flex flex-col items-center justify-center">
                        <span id="global-risk-val" class="text-5xl font-black text-white font-mono">65.2<span class="text-2xl text-red-500">%</span></span>
                        <span class="text-xs text-red-400 mt-1 font-semibold uppercase tracking-wider">심각 (Severe Crisis)</span>
                    </div>
                </div>
                
                <p class="text-xs text-gray-400 text-center mt-1">
                    전 세계 9대 요충지 교전 격화 및 군사비 증강 가중치 반영 지수
                </p>
            </div>

            <!-- 핵심 관측 지표 요약 (3개 그리드) -->
            <div class="lg:col-span-2 grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="glass-panel p-5 rounded-xl border-l-4 border-l-red-500 flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center text-gray-400 text-xs mb-1">
                            <span>활성 분쟁 지역</span>
                            <i data-lucide="flame" class="w-4 h-4 text-red-500"></i>
                        </div>
                        <div class="text-3xl font-extrabold text-white">9개 국면</div>
                    </div>
                    <div class="text-xs text-gray-400 mt-4">한반도, 우크라이나, 중동, 대만해협, 홍해 등 포함</div>
                </div>

                <div class="glass-panel p-5 rounded-xl border-l-4 border-l-amber-500 flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center text-gray-400 text-xs mb-1">
                            <span>핵·확전위험 경보</span>
                            <i data-lucide="radio" class="w-4 h-4 text-amber-500"></i>
                        </div>
                        <div class="text-3xl font-extrabold text-amber-400">LEVEL 4</div>
                    </div>
                    <div class="text-xs text-gray-400 mt-4">동북아 미사일 도발 및 중동 전면전 가능성 증대</div>
                </div>

                <div class="glass-panel p-5 rounded-xl border-l-4 border-l-cyan-500 flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center text-gray-400 text-xs mb-1">
                            <span>실시간 수집 뉴스</span>
                            <i data-lucide="newspaper" class="w-4 h-4 text-cyan-500"></i>
                        </div>
                        <div id="news-count-stat" class="text-3xl font-extrabold text-cyan-400">24건/시</div>
                    </div>
                    <div class="text-xs text-gray-400 mt-4">GDELT & 주요 통신사 AI 자동 요약 파이프라인</div>
                </div>
            </div>
        </div>

        <!-- 2. 중간: 주요 분쟁별 우세/열세(불리함) 지수 바 -->
        <div class="glass-panel p-6 rounded-2xl space-y-4">
            <h2 class="text-base font-bold text-gray-200 flex items-center gap-2">
                <i data-lucide="swords" class="w-5 h-5 text-red-400"></i> 주요 전선 전황 우세 / 열세 (Strategic Balance Bar)
            </h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-2" id="conflict-bars-container">
                <!-- 동적 카드가 생성되는 구역 -->
            </div>
        </div>

        <!-- 3. 하단: 실시간 뉴스 브리핑 타임라인 -->
        <div class="glass-panel p-6 rounded-2xl space-y-4">
            <div class="flex justify-between items-center flex-wrap gap-2">
                <h2 class="text-base font-bold text-gray-200 flex items-center gap-2">
                    <i data-lucide="zap" class="w-5 h-5 text-amber-400"></i> 실시간 감시 속보 & 주요 이슈 (Live Intelligence Feed)
                </h2>
                <span class="text-xs text-gray-400">30초 자동 갱신 중</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" id="news-feed-container">
                <!-- 뉴스 카드가 들어갈 자리 -->
            </div>
        </div>

    </main>

    <!-- 스크립트 영역 -->
    <script>
        lucide.createIcons();

        // 9대 분쟁 기본 시뮬레이션 데이터
        const conflictData = [
            { region: "한반도 & 동북아 (Korea/DMZ)", defender: "한·미 동맹", attacker: "북한·러시아", defenderRatio: 52, attackerRatio: 48, status: "미사일 도발 격화" },
            { region: "우크라이나 - 러시아 전선", defender: "우크라이나", attacker: "러시아", defenderRatio: 42, attackerRatio: 58, status: "동부 전선 소모전" },
            { region: "중동 (가자/레바논/이란)", defender: "이스라엘", attacker: "헤즈볼라·하마스·이란", defenderRatio: 55, attackerRatio: 45, status: "공습 및 전면전 위기" },
            { region: "대만 해협 (Taiwan Strait)", defender: "대만·미국", attacker: "중국", defenderRatio: 46, attackerRatio: 54, status: "해상 봉쇄 훈련 강화" },
            { region: "홍해 해상 물류 분쟁", defender: "다국적 연합군", attacker: "후티 반군", defenderRatio: 49, attackerRatio: 51, status: "상선 드론 공격 계속" }
        ];

        // 뉴스 피드 기본 데이터
        const defaultNews = [
            { title: "[한반도] 동해상 단거리 탄도미사일 포착... 전술핵 위협 수치 증가", summary: "합참은 북한이 동해상으로 신형 탄도미사일을 발사한 것을 감지했으며, 한미 연합 방위태세를 유지하고 있습니다.", region: "한반도", threat_level: 85, urgency: "위급" },
            { title: "[우크라이나] 동부 요충지 드론 집중 공격으로 에너지 기반시설 타격", summary: "러시아군의 자폭 드론 공격으로 주요 발전시설이 파괴되었으며 방공망 보충이 시급한 상황입니다.", region: "우크라이나", threat_level: 78, urgency: "경보" },
            { title: "[중동] 국경 지대 교전 격화... 민간인 대피령 발령", summary: "접경 지역에서 로켓포 및 지상군 교전이 격화되면서 유가 변동성이 급증하고 있습니다.", region: "중동", threat_level: 90, urgency: "위급" }
        ];

        // 전황 바 그리기
        function renderConflictBars() {
            const container = document.getElementById('conflict-bars-container');
            container.innerHTML = conflictData.map(c => `
                <div class="bg-gray-800/40 p-4 rounded-xl border border-gray-700/50 space-y-2">
                    <div class="flex justify-between items-center text-sm font-semibold">
                        <span class="text-gray-200">${c.region}</span>
                        <span class="text-xs px-2 py-0.5 rounded bg-gray-700 text-amber-400">${c.status}</span>
                    </div>
                    <div class="w-full bg-gray-900 h-3 rounded-full overflow-hidden flex">
                        <div class="bg-cyan-500 h-full transition-all duration-500" style="width: ${c.defenderRatio}%"></div>
                        <div class="bg-red-500 h-full transition-all duration-500" style="width: ${c.attackerRatio}%"></div>
                    </div>
                    <div class="flex justify-between text-xs text-gray-400 font-mono">
                        <span class="text-cyan-400">${c.defender}: ${c.defenderRatio}%</span>
                        <span class="text-red-400">${c.attacker}: ${c.attackerRatio}%</span>
                    </div>
                </div>
            `).join('');
        }

        // 뉴스 피드 그리기
        function renderNewsFeed(newsList) {
            const container = document.getElementById('news-feed-container');
            container.innerHTML = newsList.map(n => `
                <div class="bg-gray-800/50 hover:bg-gray-800 p-4 rounded-xl border border-gray-700/60 flex flex-col justify-between space-y-3 transition">
                    <div class="space-y-2">
                        <div class="flex justify-between items-center">
                            <span class="text-xs font-bold text-cyan-400 bg-cyan-950/60 px-2.5 py-0.5 rounded border border-cyan-800/50">${n.region}</span>
                            <span class="text-xs px-2 py-0.5 rounded font-bold ${n.urgency === '위급' ? 'bg-red-950 text-red-400 border border-red-800' : 'bg-amber-950 text-amber-400 border border-amber-800'}">${n.urgency}</span>
                        </div>
                        <h3 class="font-bold text-sm text-gray-100 line-clamp-2">${n.title}</h3>
                        <p class="text-xs text-gray-400 line-clamp-3">${n.summary}</p>
                    </div>
                    <div class="flex justify-between items-center text-xs text-gray-500 pt-2 border-t border-gray-700/40">
                        <span>위기지수: <strong class="text-red-400 font-mono">${n.threat_level}%</strong></span>
                        <span>실시간 감시</span>
                    </div>
                </div>
            `).join('');
        }

        // 파이썬 백엔드 API 통신
        async function fetchFromBackend() {
            const statusIndicator = document.getElementById('status-indicator');
            const statusText = document.getElementById('status-text');

            try {
                const res = await fetch('https://global-war-monitor.onrender.com');
                const result = await res.json();

                if (result.status === 'success') {
                    statusIndicator.className = "w-2 h-2 rounded-full bg-emerald-500";
                    statusText.innerText = "파이썬 백엔드 연동됨 (LIVE)";
                    
                    // 게이지 수치 업데이트
                    document.getElementById('global-risk-val').innerHTML = `${result.global_threat_index}<span class="text-2xl text-red-500">%</span>`;
                    
                    if (result.data && result.data.length > 0) {
                        renderNewsFeed(result.data);
                        document.getElementById('news-count-stat').innerText = `${result.data.length}건 수집`;
                    }
                }
            } catch (err) {
                statusIndicator.className = "w-2 h-2 rounded-full bg-amber-500";
                statusText.innerText = "시뮬레이션 모드 작동 중";
            }
        }

        async function triggerBackendSync() {
            try {
                await fetch('http://localhost:8000/api/conflicts/refresh', { method: 'POST' });
                alert("파이썬 백엔드로 데이터 수집 요청을 보냈습니다.");
                setTimeout(fetchFromBackend, 2000);
            } catch (err) {
                alert("백엔드 서버(http://localhost:8000)가 켜져 있는지 확인해 주세요!");
            }
        }

        // 초기화
        renderConflictBars();
        renderNewsFeed(defaultNews);
        fetchFromBackend();
        setInterval(fetchFromBackend, 10000); // 10초마다 백엔드 갱신 체크
    </script>
</body>
</html>
