import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Executive Insights: Retail Q4 Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS Y TEMATIZACIÓN ---
# Usamos un tema limpio con acentos en rojo para resaltar el problema (caída)
st.markdown("""
    <style>
    /* Estilos globales para mejorar el contraste */
    [data-testid="stAppViewContainer"] {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .stMetric {
        background-color: #1e293b !important;
        padding: 25px !important;
        border-radius: 16px !important;
        border: 1px solid #334155 !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1) !important;
    }
    /* Forzar color de texto en métricas para legibilidad */
    [data-testid="stMetricValue"] {
        color: #f8fafc !important;
        font-weight: 700 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    div[data-testid="stExpander"] {
        border: none !important;
        box-shadow: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- GENERACIÓN DE DATOS (Storytelling ready) ---
@st.cache_data
def load_and_process_data():
    """Genera dataset sintético con una caída controlada en Q4."""
    np.random.seed(42)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    regions = ['Norte', 'Sur', 'Este', 'Oeste']
    categories = ['Electrónica', 'Hogar', 'Moda', 'Alimentos']
    
    data = []
    for date in dates:
        for reg in regions:
            for cat in categories:
                # Base de ventas aleatoria (simulando variabilidad real)
                base_sales = np.random.uniform(2000, 6000)
                
                # --- INTRODUCCIÓN DE LA CAÍDA EN EL ÚLTIMO TRIMESTRE ---
                # Identificamos el último trimestre (aprox 90 días)
                is_q4 = date > (end_date - timedelta(days=90))
                
                # Aplicamos la caída específica solicitada: Región Norte y Electrónica
                if is_q4 and reg == 'Norte' and cat == 'Electrónica':
                    base_sales *= 0.70  # Caída del 30% (un poco más agresiva para impacto visual)
                
                # Simular costos y margen
                cost_ratio = np.random.uniform(0.55, 0.75)
                revenue = base_sales
                cost = revenue * cost_ratio
                
                data.append({
                    'Fecha': date,
                    'Región': reg,
                    'Categoría': cat,
                    'Ingresos': revenue,
                    'Costo': cost,
                    'Margen': revenue - cost,
                    'Ventas_Volumen': np.random.randint(10, 50)
                })
                
    df = pd.DataFrame(data)
    df['Mes'] = df['Fecha'].dt.strftime('%b')
    df['Trimestre'] = df['Fecha'].dt.quarter
    return df

# --- COMPONENTES DEL DASHBOARD ---

def sidebar_filters(df):
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3222/3222672.png", width=100)
    st.sidebar.title("Configuración de Filtros")
    st.sidebar.markdown("---")
    
    # Filtro de Fechas
    date_range = st.sidebar.date_input(
        "Rango de Análisis",
        [df['Fecha'].min().date(), df['Fecha'].max().date()],
        min_value=df['Fecha'].min().date(),
        max_value=df['Fecha'].max().date()
    )
    
    # Filtro de Categorías
    selected_cats = st.sidebar.multiselect(
        "Filtrar por Categoría",
        options=df['Categoría'].unique(),
        default=df['Categoría'].unique()
    )
    
    # Filtro de Región
    selected_regions = st.sidebar.multiselect(
        "Filtrar por Región",
        options=df['Región'].unique(),
        default=df['Región'].unique()
    )
    
    # Aplicar filtros
    mask = (df['Categoría'].isin(selected_cats)) & (df['Región'].isin(selected_regions))
    if len(date_range) == 2:
        mask = mask & (df['Fecha'].dt.date >= date_range[0]) & (df['Fecha'].dt.date <= date_range[1])
        
    return df[mask]

def render_kpis(df):
    st.subheader("📍 Resumen Ejecutivo (Último Trimestre vs Anterior)")
    
    # Cálculos de periodos
    last_90_days = df['Fecha'].max() - timedelta(days=90)
    current_q = df[df['Fecha'] >= last_90_days]
    prev_q = df[(df['Fecha'] < last_90_days) & (df['Fecha'] >= last_90_days - timedelta(days=90))]
    
    c1, c2, c3, c4 = st.columns(4)
    
    # Metricas
    def calc_delta(curr, prev):
        if prev == 0: return 0
        return ((curr - prev) / prev) * 100

    curr_rev = current_q['Ingresos'].sum()
    prev_rev = prev_q['Ingresos'].sum()
    c1.metric("Ingresos Totales", f"${curr_rev/1e6:.2f}M", f"{calc_delta(curr_rev, prev_rev):.1f}%", delta_color="normal")
    
    curr_marg = current_q['Margen'].sum()
    prev_marg = prev_q['Margen'].sum()
    c2.metric("Margen Neto", f"${curr_marg/1e6:.2f}M", f"{calc_delta(curr_marg, prev_marg):.1f}%")
    
    curr_vol = current_q['Ventas_Volumen'].sum()
    prev_vol = prev_q['Ventas_Volumen'].sum()
    c3.metric("Volumen de Ventas", f"{curr_vol:,}", f"{calc_delta(curr_vol, prev_vol):.1f}%")
    
    # Identificar foco de alerta dinámicamente
    worst_reg = current_q.groupby('Región')['Ingresos'].sum().idxmin()
    c4.metric("Región de Alerta", worst_reg, "Acción Requerida", delta_color="inverse")

def render_charts(df):
    # Gráfico 1: Tendencia Lineal (Identificando la caída)
    st.markdown("### 📉 1. Cronología del Desempeño")
    st.write("El gráfico a continuación muestra cómo la trayectoria de ingresos se desvió de las proyecciones en el último trimestre.")
    
    trend_df = df.groupby('Fecha')[['Ingresos', 'Margen']].sum().reset_index()
    fig_trend = px.line(trend_df, x='Fecha', y='Ingresos', 
                        title="Tendencia de Ingresos Diarios",
                        color_discrete_sequence=['#38bdf8'],
                        template="plotly_dark")
    
    # Resaltar zona de caída
    last_90 = df['Fecha'].max() - timedelta(days=90)
    fig_trend.add_vrect(x0=last_90, x1=df['Fecha'].max(), 
                        fillcolor="rgba(244, 63, 94, 0.2)", line_width=0,
                        annotation_text="Periodo Crítico", annotation_position="top left",
                        annotation_font_color="#fb7185")
    
    fig_trend.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color="#94a3b8"
    )
    st.plotly_chart(fig_trend, width='stretch')
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico 2: Treemap (Root Cause Analysis)
        st.markdown("### 🔍 2. Análisis Causa-Raíz (Impacto por Segmento)")
        st.write("Este Treemap permite visualizar dónde se concentra la pérdida de valor.")
        
        tree_df = df.groupby(['Región', 'Categoría'])['Ingresos'].sum().reset_index()
        fig_tree = px.treemap(tree_df, path=['Región', 'Categoría'], values='Ingresos',
                              color='Ingresos', color_continuous_scale='RdGy_r',
                              template="plotly_dark",
                              title="Distribución de Ingresos por Región y Categoría")
        
        fig_tree.update_layout(margin=dict(t=50, l=10, r=10, b=10))
        st.plotly_chart(fig_tree, width='stretch')
        
    with col2:
        # Gráfico 3: Comparativa MoM (Barras)
        st.markdown("### 📊 3. Comparativa Mensual por Categoría")
        st.write("Obsérvese la contracción específica en Electrónica comparado con otros sectores.")
        
        # Agrupar por Mes y Categoría
        month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        df['Mes'] = pd.Categorical(df['Mes'], categories=month_order, ordered=True)
        bar_df = df.groupby(['Mes', 'Categoría'])['Ingresos'].sum().reset_index()
        
        # Colores personalizados: Gris para contexto, Rojo para el problema
        color_map = {
            'Electrónica': '#f43f5e', # Rose 500 (Alerta)
            'Hogar': '#475569',      # Slate 600
            'Moda': '#64748b',      # Slate 500
            'Alimentos': '#94a3b8'   # Slate 400
        }
        
        fig_bar = px.bar(bar_df, x='Mes', y='Ingresos', color='Categoría', 
                         title="Evolución Mensual de Ingresos",
                         barmode='group',
                         template="plotly_dark",
                         color_discrete_map=color_map)
        
        fig_bar.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color="#94a3b8"
        )
        st.plotly_chart(fig_bar, width='stretch')

# --- NARRATIVA Y STORYTELLING ---

def main():
    # Carga de datos
    raw_data = load_and_process_data()
    
    # Filtros laterales
    df_filtered = sidebar_filters(raw_data)
    
    # Encabezado Principal
    st.title("🚀 Informe Estratégico: Retrospectiva Q4")
    st.markdown("""
    ---
    **Mensaje Central:** Los ingresos consolidados han experimentado una contracción atípica en el último trimestre. 
    A través de este análisis, hemos aislado el problema a una combinación específica de **geografía y línea de producto**.
    """)
    
    # 1. KPIs
    render_kpis(df_filtered)
    
    st.markdown("---")
    
    # 2. Visualizaciones Narrativas
    render_charts(df_filtered)
    
    # 3. Conclusiones y Recomendaciones
    st.markdown("---")
    st.header("💡 Recomendaciones y Plan de Acción")
    
    r1, r2, r3 = st.columns(3)
    
    with r1:
        st.error("### 🔴 Problema Identificado")
        st.write("""
        Se detectó una caída del **25-30%** en la categoría de **Electrónica** exclusivamente en la región **Norte**. 
        Otras regiones y categorías mantienen un crecimiento orgánico saludable.
        """)
        
    with r2:
        st.warning("### ⚠️ Hipótesis de Negocio")
        st.write("""
        1. **Competencia Loca:** Entrada de un nuevo retail especializado en el Norte.
        2. **Logística:** Retrasos en la cadena de suministro de componentes electrónicos detectados en Octubre.
        """)
        
    with r3:
        st.success("### ✅ Acciones Propuestas")
        st.write("""
        - **Incentivos:** Lanzar campaña de fidelización 'Norte Tech' en 48h.
        - **Auditoría:** Revisar inventario en centros de distribución Norte.
        - **Precios:** Ajustar márgenes dinámicamente en Electrónica para recuperar volumen.
        """)
    
    st.sidebar.markdown("---")
    st.sidebar.info("Dashboard diseñado por: Antigravity AI - Lead Data Scientist")

if __name__ == "__main__":
    main()
