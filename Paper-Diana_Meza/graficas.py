# ============================================
# GRÁFICOS PARA PRESENTACIÓN: METALES EN POLVO ESCOLAR (HERMOSILLO)
# ============================================

import matplotlib.pyplot as plt
import os

# Crear carpeta de salida
os.makedirs("graficas", exist_ok=True)

# 1️⃣ Gráfico de barras: comparación Norte vs Sur (Cd, Zn, Pb)
metales = ["Cd", "Zn", "Pb"]
norte = [2.83, 297, 20]
sur = [5.65, 478.93, 36.15]

plt.figure(figsize=(6,4))
x = range(len(metales))
plt.bar(x, norte, width=0.35, label="Zona Norte", color="#4C9AFF")
plt.bar([i+0.35 for i in x], sur, width=0.35, label="Zona Sur", color="#FFA726")
plt.xticks([i+0.17 for i in x], metales)
plt.ylabel("Concentración (mg/kg)")
plt.title("Comparación de concentraciones promedio de metales por zona")
plt.legend()
plt.tight_layout()
plt.savefig("graficas/grafico_barras_metales.png", dpi=300)
plt.close()


# 2️⃣ Mapa esquemático: Hermosillo norte/sur
fig, ax = plt.subplots(figsize=(5,5))
ax.set_xlim(0,10)
ax.set_ylim(0,10)

# Zonas
ax.fill_between([0,10],[5,5],[10,10], color="#4C9AFF", alpha=0.3, label="Zona Norte-Centro (Residencial)")
ax.fill_between([0,10],[0,0],[5,5], color="#FFA726", alpha=0.3, label="Zona Sur (Industrial)")

# Escuelas
ax.scatter([2,4,6,8],[8,9,7,8], c="#1565C0", marker="s", s=80, label="Escuelas")

# Fábricas
ax.scatter([3,5,7],[2,3,1], c="#E65100", marker="^", s=100, label="Industrias")

# Textos
ax.text(1,9.5,"NORTE", fontsize=12, color="#0D47A1")
ax.text(1,0.5,"SUR", fontsize=12, color="#BF360C")
ax.text(3,4.5,"Colinas La Cementera / La Flojera (barrera natural)", fontsize=8, color="gray")

ax.axis("off")
ax.legend(loc="upper right")
plt.title("Distribución esquemática de zonas y fuentes de contaminación en Hermosillo")
plt.tight_layout()
plt.savefig("graficas/mapa_esquematico_hermosillo.png", dpi=300)
plt.close()


# 3️⃣ Diagrama de fuentes (pastel)
fuentes = ["Antropogénico (Industrial / Vehicular)", "Natural"]
porcentajes = [70, 30]
colores = ["#FFA726","#81C784"]

plt.figure(figsize=(5,5))
plt.pie(porcentajes, labels=fuentes, colors=colores, autopct="%1.0f%%", startangle=90, textprops={'fontsize':10})
plt.title("Origen estimado de los metales en el polvo escolar")
plt.tight_layout()
plt.savefig("graficas/diagrama_fuentes.png", dpi=300)
plt.close()


# 4️⃣ Gráfico de riesgo relativo
metales_riesgo = ["Cd (Riñones / Huesos)", "Pb (Sistema Nervioso)", "Cr (Cáncer Potencial)", "Zn (Metabólico)"]
riesgo = [5, 4, 3, 2]  # escala simbólica
colores_riesgo = ["#E53935","#FB8C00","#FDD835","#81C784"]

plt.figure(figsize=(6,4))
plt.barh(metales_riesgo, riesgo, color=colores_riesgo)
plt.xlabel("Nivel de riesgo relativo (escala simbólica)")
plt.title("Riesgo relativo por tipo de metal y efecto en salud")
plt.tight_layout()
plt.savefig("graficas/grafico_riesgo_metales.png", dpi=300)
plt.close()

print("✅ Gráficos generados en carpeta 'graficas/'")

