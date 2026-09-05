#!/data/data/com.termux/files/usr/bin/python3

import random
import string
import os
import re
from datetime import datetime

# ==================== CONFIGURACIÓN ====================
COLOR_AZUL = "\033[34m"
COLOR_AZUL_CLARO = "\033[94m"
COLOR_RESET = "\033[0m"
COLOR_VERDE = "\033[92m"
COLOR_AMARILLO = "\033[93m"
COLOR_ROJO = "\033[91m"
COLOR_CYAN = "\033[96m"
COLOR_MAGENTA = "\033[95m"

# ==================== BANNER ====================
def mostrar_banner():
    os.system('clear')
    banner = f"""
{COLOR_AZUL_CLARO}╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   ██╗  ██╗██╗██████╗ ██╗████████╗ ██████╗               ║
║   ██║ ██╔╝██║██╔══██╗██║╚══██╔══╝██╔═══██╗              ║
║   █████╔╝ ██║██████╔╝██║   ██║   ██║   ██║              ║
║   ██╔═██╗ ██║██╔══██╗██║   ██║   ██║   ██║              ║
║   ██║  ██╗██║██║  ██║██║   ██║   ╚██████╔╝              ║
║   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝   ╚═╝    ╚═════╝               ║
║                                                           ║
║               {COLOR_VERDE}⚔️  Espadachín Negro  ⚔️{COLOR_AZUL_CLARO}                 ║
║                                                           ║
║          {COLOR_AMARILLO}✨ Generador de Combos Premium ✨{COLOR_AZUL_CLARO}          ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝{COLOR_RESET}
"""
    print(banner)

# ==================== FUNCIONES AUXILIARES ====================
def generar_nombre(longitud=8):
    """Genera un nombre aleatorio (letras mayúsculas y minúsculas)"""
    return ''.join(random.choices(string.ascii_letters, k=longitud))

def generar_numero(longitud=6):
    """Genera un número aleatorio (dígitos)"""
    return ''.join(random.choices(string.digits, k=longitud))

def generar_nombre_numero():
    """Genera un nombre con número (ej: Juan123)"""
    nombre = generar_nombre(random.randint(5, 10))
    numero = generar_numero(random.randint(2, 4))
    return nombre + numero

def generar_combo_unico(tipo):
    """Genera un combo según el tipo especificado"""
    nombre1 = generar_nombre(random.randint(4, 10))
    nombre2 = generar_nombre(random.randint(4, 10))
    numero1 = generar_numero(random.randint(3, 6))
    numero2 = generar_numero(random.randint(3, 6))
    nombre_num = generar_nombre_numero()
    
    combos = {
        1: f"{nombre1}:{nombre2}",
        2: f"{numero1}:{numero2}",
        3: f"{numero1}:{nombre1}",
        4: f"{numero1},{nombre1}",
        5: f"{numero1}:{numero2}",
        6: f"{nombre1}{numero1}:{nombre2}",
        7: f"{nombre1}:{nombre2}{numero1}",
        8: f"{numero1}:{nombre1}{numero2}"
    }
    
    return combos.get(tipo, f"{nombre1}:{nombre2}")

def generar_combo(tipo):
    """Genera un combo del tipo especificado"""
    nombre1 = generar_nombre(random.randint(4, 10))
    nombre2 = generar_nombre(random.randint(4, 10))
    numero1 = generar_numero(random.randint(3, 6))
    numero2 = generar_numero(random.randint(3, 6))
    nombre_num = generar_nombre_numero()
    
    combinaciones = [
        f"{nombre1}:{nombre2}",
        f"{numero1}:{numero2}",
        f"{numero1}:{nombre1}",
        f"{numero1},{nombre1}",
        f"{numero1}:{numero2}",
        f"{nombre1}{numero1}:{nombre2}",
        f"{nombre1}:{nombre2}{numero1}",
        f"{numero1}:{nombre1}{numero2}"
    ]
    
    return combinaciones[tipo-1]

# ==================== FUNCIONES PRINCIPALES ====================
def mostrar_tipos_combo():
    """Muestra los tipos de combo disponibles"""
    print(f"\n{COLOR_CYAN}📋 TIPOS DE COMBO DISPONIBLES:{COLOR_RESET}")
    print(f"{COLOR_AMARILLO}1.{COLOR_RESET} nombre:nombre")
    print(f"{COLOR_AMARILLO}2.{COLOR_RESET} número:número")
    print(f"{COLOR_AMARILLO}3.{COLOR_RESET} número:nombre")
    print(f"{COLOR_AMARILLO}4.{COLOR_RESET} número,nombre")
    print(f"{COLOR_AMARILLO}5.{COLOR_RESET} número:número")
    print(f"{COLOR_AMARILLO}6.{COLOR_RESET} nombre número:nombre")
    print(f"{COLOR_AMARILLO}7.{COLOR_RESET} nombre:nombre número")
    print(f"{COLOR_AMARILLO}8.{COLOR_RESET} número:nombre número")

def crear_combo():
    """Función principal para crear combos"""
    mostrar_banner()
    
    # Mostrar tipos de combo
    mostrar_tipos_combo()
    
    # Seleccionar tipo
    while True:
        try:
            print(f"\n{COLOR_VERDE}🔢 Selecciona el tipo de combo (1-8):{COLOR_RESET}")
            tipo = int(input(f"{COLOR_AZUL_CLARO}➜ {COLOR_RESET}"))
            if 1 <= tipo <= 8:
                break
            else:
                print(f"{COLOR_ROJO}❌ Error: Elige un número entre 1 y 8{COLOR_RESET}")
        except ValueError:
            print(f"{COLOR_ROJO}❌ Error: Ingresa un número válido{COLOR_RESET}")
    
    # Preguntar cantidad
    while True:
        try:
            print(f"\n{COLOR_VERDE}🔢 ¿Cuántos combos deseas generar?{COLOR_RESET}")
            cantidad = int(input(f"{COLOR_AZUL_CLARO}➜ {COLOR_RESET}"))
            if cantidad > 0:
                break
            else:
                print(f"{COLOR_ROJO}❌ Error: La cantidad debe ser mayor a 0{COLOR_RESET}")
        except ValueError:
            print(f"{COLOR_ROJO}❌ Error: Ingresa un número válido{COLOR_RESET}")
    
    # Generar combos
    print(f"\n{COLOR_VERDE}⏳ Generando combos...{COLOR_RESET}")
    combos_generados = []
    for _ in range(cantidad * 3):  # Generar más para asegurar cantidad después de eliminar duplicados
        combos_generados.append(generar_combo(tipo))
    
    # Eliminar duplicados
    combos_unicos = list(set(combos_generados))
    
    # Asegurar que tengamos la cantidad solicitada
    while len(combos_unicos) < cantidad:
        combos_unicos.append(generar_combo(tipo))
        combos_unicos = list(set(combos_unicos))
    
    # Ordenar por números
    combos_unicos.sort(key=lambda x: re.findall(r'\d+', x))
    
    # Mostrar combos
    print(f"\n{COLOR_CYAN}📋 COMBOS GENERADOS:{COLOR_RESET}")
    for i, combo in enumerate(combos_unicos[:cantidad], 1):
        print(f"{COLOR_VERDE}{i}.{COLOR_RESET} {combo}")
    
    # Guardar en archivo
    guardar_combo(combos_unicos[:cantidad])
    
    print(f"\n{COLOR_VERDE}✅ ¡Proceso completado exitosamente! 🎉{COLOR_RESET}")

def guardar_combo(combos):
    """Guarda los combos en un archivo"""
    # Crear carpeta Combo fuera de termux
    carpeta_combo = "/sdcard/Combo"  # Ruta para Android
    if not os.path.exists(carpeta_combo):
        try:
            os.makedirs(carpeta_combo)
            print(f"{COLOR_VERDE}📁 Carpeta 'Combo' creada en /sdcard/{COLOR_RESET}")
        except:
            # Si no se puede crear en /sdcard, usar ruta alternativa
            carpeta_combo = os.path.expanduser("~/Combo")
            if not os.path.exists(carpeta_combo):
                os.makedirs(carpeta_combo)
                print(f"{COLOR_VERDE}📁 Carpeta 'Combo' creada en ~/Combo{COLOR_RESET}")
    
    # Elegir nombre de archivo
    print(f"\n{COLOR_CYAN}📝 Elige el nombre para el archivo (sin extensión):{COLOR_RESET}")
    print(f"{COLOR_AMARILLO}💡 Presiona Enter para usar 'kirito.txt'{COLOR_RESET}")
    nombre_archivo = input(f"{COLOR_AZUL_CLARO}➜ {COLOR_RESET}")
    
    if not nombre_archivo.strip():
        nombre_archivo = "kirito"
    
    # Asegurar extensión .txt
    if not nombre_archivo.endswith('.txt'):
        nombre_archivo += '.txt'
    
    ruta_completa = os.path.join(carpeta_combo, nombre_archivo)
    
    # Guardar archivo
    try:
        with open(ruta_completa, 'w') as f:
            f.write(f"=== COMBOS GENERADOS ===\n")
            f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total de combos: {len(combos)}\n")
            f.write("="*50 + "\n\n")
            
            for i, combo in enumerate(combos, 1):
                f.write(f"{i}. {combo}\n")
        
        print(f"\n{COLOR_VERDE}✅ Archivo guardado en: {ruta_completa} 📁{COLOR_RESET}")
        print(f"{COLOR_VERDE}🎉 ¡Combos guardados exitosamente!{COLOR_RESET}")
        
    except Exception as e:
        print(f"{COLOR_ROJO}❌ Error al guardar el archivo: {e}{COLOR_RESET}")
        print(f"{COLOR_AMARILLO}💡 Intentando guardar en la carpeta actual...{COLOR_RESET}")
        
        # Intentar guardar en carpeta actual como respaldo
        try:
            with open(nombre_archivo, 'w') as f:
                f.write(f"=== COMBOS GENERADOS ===\n")
                f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total de combos: {len(combos)}\n")
                f.write("="*50 + "\n\n")
                
                for i, combo in enumerate(combos, 1):
                    f.write(f"{i}. {combo}\n")
            
            print(f"{COLOR_VERDE}✅ Archivo guardado en carpeta actual: {nombre_archivo} 📁{COLOR_RESET}")
        except Exception as e2:
            print(f"{COLOR_ROJO}❌ Error al guardar el archivo: {e2}{COLOR_RESET}")

# ==================== MENÚ PRINCIPAL ====================
def menu_principal():
    """Menú principal del programa"""
    while True:
        mostrar_banner()
        
        print(f"\n{COLOR_CYAN}📋 MENÚ PRINCIPAL:{COLOR_RESET}")
        print(f"{COLOR_VERDE}1.{COLOR_RESET} 🆕 Crear nuevos combos")
        print(f"{COLOR_VERDE}2.{COLOR_RESET} ℹ️  Información")
        print(f"{COLOR_VERDE}3.{COLOR_RESET} 🚪 Salir")
        
        opcion = input(f"\n{COLOR_AZUL_CLARO}➜ Selecciona una opción: {COLOR_RESET}")
        
        if opcion == "1":
            crear_combo()
            input(f"\n{COLOR_AMARILLO}🔄 Presiona Enter para continuar...{COLOR_RESET}")
        elif opcion == "2":
            print(f"\n{COLOR_CYAN}📖 INFORMACIÓN:{COLOR_RESET}")
            print(f"{COLOR_AMARILLO}⚔️ KIRITO - Espadachín Negro{COLOR_RESET}")
            print(f"{COLOR_VERDE}📌 Generador de combos para termux{COLOR_RESET}")
            print(f"{COLOR_CYAN}✨ Creado con ❤️ para la comunidad{COLOR_RESET}")
            print(f"{COLOR_MAGENTA}🎯 Versión 1.0{COLOR_RESET}")
            input(f"\n{COLOR_AMARILLO}🔄 Presiona Enter para continuar...{COLOR_RESET}")
        elif opcion == "3":
            print(f"\n{COLOR_VERDE}👋 ¡Hasta luego! ⚔️{COLOR_RESET}")
            break
        else:
            print(f"{COLOR_ROJO}❌ Opción inválida{COLOR_RESET}")
            input(f"\n{COLOR_AMARILLO}🔄 Presiona Enter para continuar...{COLOR_RESET}")

# ==================== EJECUCIÓN PRINCIPAL ====================
if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n\n{COLOR_AMARILLO}⛔ Programa interrumpido por el usuario{COLOR_RESET}")
        print(f"{COLOR_VERDE}👋 ¡Hasta luego! ⚔️{COLOR_RESET}")
    except Exception as e:
        print(f"\n{COLOR_ROJO}❌ Error inesperado: {e}{COLOR_RESET}")
        input(f"\n{COLOR_AMARILLO}🔄 Presiona Enter para salir...{COLOR_RESET}")