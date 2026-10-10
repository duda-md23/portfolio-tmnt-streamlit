import json
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

# -----------------------------------------------------------------------------
# 1. CONFIGURAÇÃO DA PÁGINA STREAMLIT
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Maria Eduarda Rocha | TMNT Data & Cyber Lab",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# 2. ESTILIZAÇÃO CSS CUSTOMIZADA (TEMA DARK / TMNT CYBERPUNK)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&display=swap');

    /* Fundo da aplicação */
    .stApp {
        background-color: #0b0f19;
        font-family: 'Fira Code', monospace;
        color: #e2e8f0;
    }

    /* Ocultar elementos desnecessários do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Sidebar estilizada */
    section[data-testid="stSidebar"] {
        background-color: #070a12;
        border-right: 1px solid #1e293b;
    }

    /* Cartões temáticos */
    .ninja-card {
        padding: 1.25rem;
        border-radius: 8px;
        background: #111827;
        margin-bottom: 1rem;
        transition: transform 0.25s ease, border-color 0.25s ease;
    }
    .ninja-card:hover {
        transform: translateY(-3px);
    }
    .card-donatello { border: 1px solid rgba(168, 85, 247, 0.4); }
    .card-raphael   { border: 1px solid rgba(239, 68, 68, 0.4); }
    .card-leonardo  { border: 1px solid rgba(59, 130, 246, 0.4); }
    .card-mikey     { border: 1px solid rgba(249, 115, 22, 0.4); }

    /* Badges */
    .badge-tag {
        display: inline-block;
        font-size: 0.72rem;
        background: #1e293b;
        color: #4ade80;
        border: 1px solid #334155;
        padding: 2px 8px;
        border-radius: 4px;
        margin: 2px 4px 2px 0;
    }

    /* Terminal container */
    .terminal-box {
        background-color: #030712;
        border: 1px solid #22c55e;
        border-radius: 6px;
        padding: 1rem;
        font-family: 'Fira Code', monospace;
        color: #22c55e;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. SIDEBAR (PERFIL & CONTATO)
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### `// INFORMAÇÕES_OPERADOR`")
    st.markdown("**Maria Eduarda de Andrade Rocha**")
    st.caption("Especialista em Dados, Cybersecurity & Operações de TI")
    
    st.markdown("---")
    st.markdown("#### 🔗 Links Oficiais")
    st.markdown("- [GitHub](https://github.com/duda-md23)")
    st.markdown("- [LinkedIn](https://linkedin.com/in/eduarda-andrade-ti)")
    st.markdown("- [E-mail](mailto:eduardaandrade934@gmail.com)")
    
    st.markdown("---")
    st.markdown("#### 🛠️ Stack Principal")
    badges = [
        "Python (Pandas, NumPy)", "SQL", "Power BI", "Excel Avançado",
        "Cybersecurity", "Active Directory", "GLPI", "Linux"
    ]
    st.markdown("".join([f"<span class='badge-tag'>{b}</span>" for b in badges]), unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. CABEÇALHO & CANVAS 3D INTERATIVO (THREE.JS MUTAGÊNIO)
# -----------------------------------------------------------------------------
col_header, col_3d = st.columns([1.4, 1.0], gap="medium")

with col_header:
    st.markdown("<p style='color: #22c55e; font-weight: 700; margin-bottom: 0;'>&lt;TMNT_SEWERS / DATA_LAB&gt;</p>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: white; font-size: 2.2rem; margin-top: 0;'>MARIA EDUARDA ROCHA</h1>", unsafe_allow_html=True)
    st.markdown("""
    Unindo a engenharia analítica de **Donatello** (Python, SQL e automações) à vigilância proativa de **Raphael** contra anomalias e riscos.
    Foco em construção de pipelines confiáveis, auditorias analíticas e infraestrutura resiliente.
    """)
    st.info("💡 **Dica de Interação:** O reator mutagênico 3D à direita responde ao movimento do seu mouse. Clique e arraste para rotacionar.")

with col_3d:
    # Componente 3D Three.js integrado diretamente via WebGL
    threejs_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body { margin: 0; overflow: hidden; background: transparent; }
            canvas { width: 100%; height: 100%; display: block; }
        </style>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    </head>
    <body>
        <div id="canvas-container"></div>
        <script>
            const container = document.getElementById('canvas-container');
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / 280, 0.1, 1000);
            camera.position.set(0, 2.5, 5);

            const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
            renderer.setSize(window.innerWidth, 280);
            container.appendChild(renderer.domElement);

            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.enableZoom = false;

            // Iluminação
            const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
            scene.add(ambientLight);
            const pointLight = new THREE.PointLight(0x22c55e, 2, 50);
            pointLight.position.set(2, 4, 3);
            scene.add(pointLight);

            // Tampa do Bueiro / Núcleo
            const cylinderGeo = new THREE.CylinderGeometry(1.5, 1.5, 0.25, 32);
            const cylinderMat = new THREE.MeshStandardMaterial({ color: 0x1f2937, roughness: 0.4, metalness: 0.8 });
            const cylinder = new THREE.Mesh(cylinderGeo, cylinderMat);
            scene.add(cylinder);

            // Anéis de Mutagênio Neon
            const ringGeo = new THREE.TorusGeometry(1.65, 0.05, 16, 64);
            const ringMat = new THREE.MeshBasicMaterial({ color: 0x22c55e, wireframe: true });
            const ring = new THREE.Mesh(ringGeo, ringMat);
            ring.rotation.x = Math.PI / 2;
            scene.add(ring);

            // Anel Orbital Externo
            const orbitGeo = new THREE.TorusGeometry(2.1, 0.02, 16, 64);
            const orbitMat = new THREE.MeshBasicMaterial({ color: 0xa855f7 });
            const orbitRing = new THREE.Mesh(orbitGeo, orbitMat);
            orbitRing.rotation.x = Math.PI / 3;
            scene.add(orbitRing);

            function animate() {
                requestAnimationFrame(animate);
                cylinder.rotation.y += 0.005;
                ring.rotation.z += 0.01;
                orbitRing.rotation.y += 0.008;
                controls.update();
                renderer.render(scene, camera);
            }
            animate();

            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / 280;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, 280);
            });
        </script>
    </body>
    </html>
    """
    components.html(threejs_code, height=290, scrolling=False)

st.markdown("---")

# -----------------------------------------------------------------------------
# 5. OS 4 PILARES TÉCNICOS (TMNT QUAD)
# -----------------------------------------------------------------------------
st.markdown("### `// PILARES_TÉCNICOS (THE NINJA QUAD)`")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="ninja-card card-donatello">
        <h4 style="color: #c084fc; margin-top:0;">🟣 DONATELLO</h4>
        <strong style="color: #f3e8ff; font-size: 0.85rem;">Engenharia de Dados & IA</strong>
        <p style="color: #94a3b8; font-size: 0.78rem; margin-top: 0.5rem;">
            Pipelines ETL automatizados, modelagem relacional em SQL, Pandas/NumPy para higienização analítica e automações.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="ninja-card card-raphael">
        <h4 style="color: #f87171; margin-top:0;">🔴 RAPHAEL</h4>
        <strong style="color: #fee2e2; font-size: 0.85rem;">Cybersecurity & Risco</strong>
        <p style="color: #94a3b8; font-size: 0.78rem; margin-top: 0.5rem;">
            Mitigação de vulnerabilidades, detecção estatística de outliers, auditoria de transações e prevenção a fraudes operacionais.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="ninja-card card-leonardo">
        <h4 style="color: #60a5fa; margin-top:0;">🔵 LEONARDO</h4>
        <strong style="color: #dbeafe; font-size: 0.85rem;">Governança & Infra</strong>
        <p style="color: #94a3b8; font-size: 0.78rem; margin-top: 0.5rem;">
            Administração de Active Directory (AD), políticas RBAC, sustentação em Linux, conformidade de redes e padronização.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="ninja-card card-mikey">
        <h4 style="color: #fb923c; margin-top:0;">🟠 MICHELANGELO</h4>
        <strong style="color: #ffedd5; font-size: 0.85rem;">Operação & Suporte N2</strong>
        <p style="color: #94a3b8; font-size: 0.78rem; margin-top: 0.5rem;">
            Gestão ágil de incidentes críticos, tickets via GLPI, garantia de SLA rigoroso e comunicação técnica transparente.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. LABORATÓRIO INTERATIVO: DETECÇÃO DE OUTLIERS (DEMONSTRAÇÃO PRÁTICA)
# -----------------------------------------------------------------------------
st.markdown("### `// LAB_INTERATIVO: AUDITORIA & DETECÇÃO DE RISCO`")
st.caption("Demonstração prática em execução real de Pandas/NumPy: simulação de tráfego/transações e isolamento de anomalias estatísticas.")

with st.expander("🔬 Abrir Painel de Simulação de Auditoria", expanded=True):
    col_ctrl, col_graph = st.columns([1, 2])
    
    with col_ctrl:
        num_pontos = st.slider("Volume de Transações Analisadas:", min_value=100, max_value=1000, value=300, step=50)
        desvio_corte = st.slider("Limiar de Desvio Padrão (Z-Score):", min_value=1.5, max_value=3.5, value=2.2, step=0.1)
        
        # Geração de dados de teste determinística
        np.random.seed(42)
        base_valores = np.random.normal(loc=150, scale=25, size=num_pontos)
        # Inserção proposital de outliers
        outlier_indices = np.random.choice(num_pontos, size=int(num_pontos * 0.05), replace=False)
        base_valores[outlier_indices] += np.random.choice([-1, 1], size=len(outlier_indices)) * np.random.uniform(70, 160, size=len(outlier_indices))
        
        df_sim = pd.DataFrame({
            "ID_Transacao": [f"TX-{i:04d}" for i in range(num_pontos)],
            "Valor": np.round(base_valores, 2)
        })
        
        # Algoritmo de identificação
        media = df_sim["Valor"].mean()
        desvio = df_sim["Valor"].std()
        df_sim["Z_Score"] = (df_sim["Valor"] - media) / desvio
        df_sim["Anomalia"] = df_sim["Z_Score"].abs() > desvio_corte
        
        anomalias_detectadas = int(df_sim["Anomalia"].sum())
        st.metric(label="Anomalias Detectadas", value=anomalias_detectadas, delta=f"{anomalias_detectadas/num_pontos*100:.1f}% do total")
    
    with col_graph:
        st.line_chart(df_sim[["Valor"]])
        if anomalias_detectadas > 0:
            st.warning(f"🚨 Raphael Alerta: {anomalias_detectadas} registros excederam o limiar de risco estatístico.")
            st.dataframe(df_sim[df_sim["Anomalia"]][["ID_Transacao", "Valor", "Z_Score"]].head(5), use_container_width=True)

# -----------------------------------------------------------------------------
# 7. PROJETOS EM DESTAQUE
# -----------------------------------------------------------------------------
st.markdown("### `// PROJETOS_EM_DESTAQUE`")

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
    **Automação de Auditoria e Limpeza de Dados**  
    `Python • Pandas • NumPy`  
    Script analítico para higienização e validação de relatórios volumosos, cruzamento de bases transacionais e identificação de anomalias com 95% de ganho de tempo.
    """)
    st.markdown("[Ver no GitHub →](https://github.com/duda-md23)")

with p2:
    st.markdown("""
    **Governança & Hardening de Active Directory**  
    `Active Directory • Cybersecurity • RBAC`  
    Reestruturação de florestas de usuários, padronização de GPOs, auditoria de privilégios e blindagem contra escalada de privilégios.
    """)
    st.markdown("[Ver no GitHub →](https://github.com/duda-md23)")

with p3:
    st.markdown("""
    **Dashboard de Gestão de Incidentes & SLA**  
    `Power BI • GLPI • SQL`  
    Visão executiva em tempo real monitorando volumetria de chamados N2, gargalos operacionais e cumprimento estrito de SLA contratual.
    """)
    st.markdown("[Ver no GitHub →](https://github.com/duda-md23)")

# -----------------------------------------------------------------------------
# 8. RODAPÉ
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    "<center style='color: #64748b; font-size: 0.8rem;'>"
    "© 2026 Maria Eduarda de Andrade Rocha • Desenvolvido com Streamlit & Three.js"
    "</center>",
    unsafe_allow_html=True
)