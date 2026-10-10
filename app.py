import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Maria Eduarda | Data & Cybersecurity Lab",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# ESTILIZAÇÃO HUD / CYBERPUNK TMNT
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Fira Code', monospace;
        color: #e2e8f0;
    }
    .stApp {
        background: radial-gradient(circle at 50% 20%, #0d1527 0%, #060911 100%);
    }
    
    /* Headers & Textos */
    h1, h2, h3 {
        font-family: 'Fira Code', monospace !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
    }
    
    /* Efeito Glassmorphism dos Cards */
    .hud-card {
        background: rgba(13, 21, 39, 0.7);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(34, 197, 94, 0.25);
        border-radius: 12px;
        padding: 20px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 16px;
    }
    .hud-card:hover {
        border-color: #22c55e;
        box-shadow: 0 0 20px rgba(34, 197, 94, 0.25);
        transform: translateY(-3px);
    }
    
    .hud-tag {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        margin-right: 6px;
        margin-bottom: 6px;
        border: 1px solid;
    }
    .tag-dona { background: rgba(168, 85, 247, 0.15); border-color: #a855f7; color: #d8b4fe; }
    .tag-raph { background: rgba(239, 68, 68, 0.15); border-color: #ef4444; color: #fca5a5; }
    .tag-leo  { background: rgba(59, 130, 246, 0.15); border-color: #3b82f6; color: #93c5fd; }
    .tag-mike { background: rgba(249, 115, 22, 0.15); border-color: #f97316; color: #fdba74; }
    
    /* Métricas do Streamlit */
    [data-testid="stMetricValue"] {
        color: #22c55e !important;
        font-family: 'Fira Code', monospace !important;
        font-size: 26px !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# CENA 3D IMERSIVA (THREE.JS + PARTÍCULAS MUTAGÊNICAS)
# ==========================================
three_canvas_html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body, html { margin: 0; padding: 0; overflow: hidden; background: transparent; }
        #canvas-container { width: 100vw; height: 380px; position: relative; }
        #overlay-hud {
            position: absolute;
            bottom: 15px;
            left: 20px;
            color: #22c55e;
            font-family: 'Fira Code', monospace;
            font-size: 11px;
            pointer-events: none;
            text-shadow: 0 0 8px rgba(34,197,94,0.6);
        }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
    <div id="canvas-container">
        <div id="overlay-hud">● NÚCLEO MUTAGÊNICO ATIVO // ARRASTE O MOUSE PARA ROTACIONAR (ORBIT 3D)</div>
    </div>
    <script>
        const container = document.getElementById('canvas-container');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
        camera.position.set(0, 3, 7);

        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setSize(container.clientWidth, container.clientHeight);
        renderer.setPixelRatio(window.devicePixelRatio);
        container.appendChild(renderer.domElement);

        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.autoRotate = true;
        controls.autoRotateSpeed = 1.2;
        controls.maxDistance = 12;
        controls.minDistance = 3;

        // Luzes
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
        scene.add(ambientLight);

        const greenLight = new THREE.PointLight(0x22c55e, 2, 50);
        greenLight.position.set(0, 2, 2);
        scene.add(greenLight);

        const purpleLight = new THREE.PointLight(0xa855f7, 1.5, 50);
        purpleLight.position.set(-3, -2, -2);
        scene.add(purpleLight);

        // Grupo do Reator / Bueiro 3D
        const group = new THREE.Group();

        // Núcleo central (Icosaedro de Mutagênio)
        const coreGeo = new THREE.IcosahedronGeometry(1.2, 1);
        const coreMat = new THREE.MeshStandardMaterial({
            color: 0x22c55e,
            wireframe: true,
            emissive: 0x15803d,
            roughness: 0.2
        });
        const core = new THREE.Mesh(coreGeo, coreMat);
        group.add(core);

        // Anel Órbita 1 (Donatello - Roxo)
        const ring1Geo = new THREE.TorusGeometry(2.0, 0.03, 16, 100);
        const ring1Mat = new THREE.MeshBasicMaterial({ color: 0xa855f7 });
        const ring1 = new THREE.Mesh(ring1Geo, ring1Mat);
        ring1.rotation.x = Math.PI / 3;
        group.add(ring1);

        // Anel Órbita 2 (Raphael - Vermelho)
        const ring2Geo = new THREE.TorusGeometry(2.5, 0.03, 16, 100);
        const ring2Mat = new THREE.MeshBasicMaterial({ color: 0xef4444 });
        const ring2 = new THREE.Mesh(ring2Geo, ring2Mat);
        ring2.rotation.y = Math.PI / 4;
        group.add(ring2);

        // Anel Órbita 3 (Leonardo - Azul)
        const ring3Geo = new THREE.TorusGeometry(3.0, 0.03, 16, 100);
        const ring3Mat = new THREE.MeshBasicMaterial({ color: 0x3b82f6 });
        const ring3 = new THREE.Mesh(ring3Geo, ring3Mat);
        ring3.rotation.x = -Math.PI / 4;
        group.add(ring3);

        // Partículas Flutuantes de Dados no Esgoto
        const particlesCount = 200;
        const pGeo = new THREE.BufferGeometry();
        const pPos = new Float32Array(particlesCount * 3);

        for(let i = 0; i < particlesCount * 3; i++) {
            pPos[i] = (Math.random() - 0.5) * 14;
        }
        pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
        const pMat = new THREE.PointsMaterial({
            size: 0.05,
            color: 0x22c55e,
            transparent: true,
            opacity: 0.8
        });
        const particles = new THREE.Points(pGeo, pMat);
        scene.add(particles);

        scene.add(group);

        // Loop de Renderização
        function animate() {
            requestAnimationFrame(animate);
            core.rotation.y += 0.005;
            core.rotation.x += 0.003;
            ring1.rotation.z += 0.008;
            ring2.rotation.x += 0.006;
            ring3.rotation.y += 0.007;
            particles.rotation.y += 0.001;
            controls.update();
            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('resize', () => {
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(container.clientWidth, container.clientHeight);
        });
    </script>
</body>
</html>
"""

# ==========================================
# BARRA SUPERIOR & HERO HUD
# ==========================================
col_brand, col_links = st.columns([2, 1])
with col_brand:
    st.markdown("<h2 style='color:#22c55e; margin:0;'>&lt;TMNT_SEWERS // DATA_CYBER_LAB&gt;</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b; font-size:13px;'>SECURE ANALYTICS & THREAT DEFENSE PORTFOLIO</p>", unsafe_allow_html=True)

with col_links:
    st.markdown("""
    <div style='text-align:right; padding-top:10px;'>
        <a href='https://github.com/duda-md23' target='_blank' style='color:#22c55e; text-decoration:none; margin-right:15px; font-weight:600;'>[GitHub]</a>
        <a href='https://linkedin.com/in/eduarda-andrade-ti' target='_blank' style='color:#38bdf8; text-decoration:none; margin-right:15px; font-weight:600;'>[LinkedIn]</a>
        <a href='mailto:eduardaandrade934@gmail.com' style='color:#cbd5e1; text-decoration:none; font-weight:600;'>[E-mail]</a>
    </div>
    """, unsafe_allow_html=True)

# Renderiza o 3D Imersivo
components.html(three_canvas_html, height=380)

# Resumo do Perfil
st.markdown("""
<div class='hud-card' style='border-left: 4px solid #22c55e;'>
    <h3 style='color:white; margin:0 0 8px 0;'>MARIA EDUARDA DE ANDRADE ROCHA</h3>
    <p style='color:#94a3b8; font-size:14px; line-height:1.6; margin-bottom:12px;'>
        Especialista em <b>Análise de Dados</b>, <b>Cybersecurity / Risco</b> e <b>Sustentação N2</b>. 
        Construo arquiteturas analíticas blindadas, automações resilientes com Python e estratégias de detecção de anomalias que mitigam riscos operacionais e financeiros.
    </p>
    <div>
        <span class='hud-tag tag-dona'>Python (Pandas/NumPy)</span>
        <span class='hud-tag tag-dona'>SQL Avançado</span>
        <span class='hud-tag tag-raph'>Detecção de Outliers</span>
        <span class='hud-tag tag-raph'>Auditoria & Risco</span>
        <span class='hud-tag tag-leo'>Active Directory (AD)</span>
        <span class='hud-tag tag-mike'>SLA & Suporte N2 (GLPI)</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# PILARES TÉCNICOS (AS 4 TARTARUGAS)
# ==========================================
st.markdown("<h4 style='color:#22c55e; margin-top:20px;'>// ARQUITETURA TÉCNICA (PILARES TMNT)</h4>", unsafe_allow_html=True)

col_dona, col_raph, col_leo, col_mike = st.columns(4)

with col_dona:
    st.markdown("""
    <div class='hud-card' style='border-color: rgba(168, 85, 247, 0.4);'>
        <div style='color:#a855f7; font-weight:700; font-size:13px;'>[DONATELLO]</div>
        <div style='color:white; font-weight:600; font-size:14px; margin:4px 0 8px;'>Engenharia & Dados</div>
        <div style='color:#94a3b8; font-size:12px; line-height:1.5;'>
            Automação de ETL, modelagem relacional, higienização massiva com Pandas e desenvolvimento de algoritmos analíticos.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_raph:
    st.markdown("""
    <div class='hud-card' style='border-color: rgba(239, 68, 68, 0.4);'>
        <div style='color:#ef4444; font-weight:700; font-size:13px;'>[RAPHAEL]</div>
        <div style='color:white; font-weight:600; font-size:14px; margin:4px 0 8px;'>Cybersecurity & Risco</div>
        <div style='color:#94a3b8; font-size:12px; line-height:1.5;'>
            Auditoria estatística em iGaming/finanças, monitoramento de discrepâncias, prevenção a fraudes e análise de vulnerabilidades.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_leo:
    st.markdown("""
    <div class='hud-card' style='border-color: rgba(59, 130, 246, 0.4);'>
        <div style='color:#3b82f6; font-weight:700; font-size:13px;'>[LEONARDO]</div>
        <div style='color:white; font-weight:600; font-size:14px; margin:4px 0 8px;'>Governança & Infra</div>
        <div style='color:#94a3b8; font-size:12px; line-height:1.5;'>
            Gestão de acessos (RBAC) via Active Directory (AD), suporte a ambientes Linux e controle de políticas de rede corporativa.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_mike:
    st.markdown("""
    <div class='hud-card' style='border-color: rgba(249, 115, 22, 0.4);'>
        <div style='color:#f97316; font-weight:700; font-size:13px;'>[MICHELANGELO]</div>
        <div style='color:white; font-weight:600; font-size:14px; margin:4px 0 8px;'>Operações & SLA N2</div>
        <div style='color:#94a3b8; font-size:12px; line-height:1.5;'>
            Gestão e resolução ágil de incidentes críticos, fluxos em GLPI e garantia rigorosa de prazos de atendimento (SLA).
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# TERMINAL INTERATIVO CLI (SOC SHELL)
# ==========================================
st.markdown("<h4 style='color:#22c55e; margin-top:25px;'>// DONATELLO TERMINAL CLI</h4>", unsafe_allow_html=True)

with st.container():
    cli_col1, cli_col2 = st.columns([3, 1])
    with cli_col1:
        cmd_input = st.text_input("Digite um comando (ex: help, skills, projects, audit, contact):", value="help", key="cli_cmd")
    with cli_col2:
        st.write("")
        st.write("")
        run_btn = st.button("Executar Comando", use_container_width=True)

    cmd = cmd_input.strip().lower()
    cli_output = ""

    if cmd == "help":
        cli_output = """
        COMANDOS DISPONÍVEIS NO SOC_TERMINAL:
        - whoami    : Exibe detalhes do perfil profissional.
        - skills    : Lista a stack tecnológica categorizada por pilar.
        - projects  : Lista os projetos em destaque e seus repositórios.
        - audit     : Executa uma rotina rápida de integridade nos logs.
        - contact   : Mostra os canais de comunicação direta.
        - pizza     : Mensagem especial da base dos esgotos.
        """
    elif cmd == "whoami":
        cli_output = "USER: Maria Eduarda de Andrade Rocha\nROLE: Data Analytics, Cybersecurity & N2 Ops\nLOCATION: Brasil\nSTATUS: Disponível para novos desafios técnicos."
    elif cmd == "skills":
        cli_output = "CORE: Python (Pandas, NumPy, Streamlit), SQL, Power BI\nSECURITY: Detecção de Fraude, Análise de Risco, Auditoria de Outliers\nINFRA: Active Directory, Linux, GLPI, Redes e Governança RBAC."
    elif cmd == "projects":
        cli_output = "[1] Automação de Auditoria e Higienização de Transações (Python/Pandas)\n[2] Painel Gerencial de Incidentes e SLA (Power BI / GLPI)\n[3] Governança e Blindagem de Acessos via Active Directory"
    elif cmd == "audit":
        cli_output = "[LOG SCAN] 1.000 registros verificados...\n[INTEGRIDADE] Nenhuma vulnerabilidade crítica detectada.\n[STATUS] Perímetro monitorado com sucesso."
    elif cmd == "contact":
        cli_output = "LinkedIn: linkedin.com/in/eduarda-andrade-ti\nGitHub: github.com/duda-md23\nE-mail: eduardaandrade934@gmail.com"
    elif cmd == "pizza":
        cli_output = "Cowabunga! 🍕 A energia que move o laboratório entre uma consulta SQL e um pipeline Python."
    else:
        cli_output = f"Comando '{cmd}' não reconhecido. Digite 'help' para listar as opções."

    st.code(cli_output, language="bash")

# ==========================================
# LABORATÓRIO PRÁTICO INTERATIVO DE ANÁLISE & RISCO
# ==========================================
st.markdown("<h4 style='color:#22c55e; margin-top:25px;'>// SOC DATA LAB (SIMULADOR DE RISCO & ANOMALIAS)</h4>", unsafe_allow_html=True)

tab_lab, tab_projetos = st.tabs(["[SIMULADOR DE TRANSAÇÕES & OUTLIERS]", "[CASES DE PROJETOS]"])

with tab_lab:
    st.markdown("<p style='color:#94a3b8; font-size:13px;'>Interaja com o algoritmo abaixo para inspecionar transações em tempo real e isolar anomalias financeiras/operacionais:</p>", unsafe_allow_html=True)
    
    col_ctrl1, col_ctrl2 = st.columns(2)
    with col_ctrl1:
        n_samples = st.slider("Volume de Transações Monitoradas:", min_value=100, max_value=2000, value=600, step=100)
    with col_ctrl2:
        threshold = st.slider("Limiar de Desvio Z-Score para Risco:", min_value=1.5, max_value=3.5, value=2.2, step=0.1)

    # Geração dos dados
    np.random.seed(42)
    base_values = np.random.normal(loc=120, scale=30, size=n_samples)
    outlier_idx = np.random.choice(n_samples, size=int(n_samples * 0.05), replace=False)
    base_values[outlier_idx] += np.random.uniform(100, 350, size=len(outlier_idx))

    df = pd.DataFrame({
        "Transacao_ID": [f"TX-{1000 + i}" for i in range(n_samples)],
        "Valor_BRL": np.round(base_values, 2),
        "Categoria": np.random.choice(["Operacional", "iGaming", "Transferência", "Taxa"], size=n_samples)
    })

    # Cálculo estatístico
    mean_val = df["Valor_BRL"].mean()
    std_val = df["Valor_BRL"].std()
    df["Z_Score"] = ((df["Valor_BRL"] - mean_val) / std_val).round(2)