import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda_project.settings')
django.setup()

from productos.models import Producto

def poblar_catalogo():
    print("=" * 70)
    print("SCRIPT DE POBLADO DE DATOS Y CONSULTAS ORM - DJANGO 5.x")
    print("Estudiante: Arlette Suárez Román | UNCP FIS")
    print("=" * 70)

    # Limpiar registros previos si existen
    Producto.objects.all().delete()
    print("[*] Base de datos SQLite reiniciada con éxito.")

    # Lista de productos de prueba representativos
    productos_data = [
        {
            "nombre": "Laptop ASUS ROG Zephyrus G14",
            "descripcion": "Procesador AMD Ryzen 9, 32GB RAM DDR5, 1TB SSD NVMe, NVIDIA RTX 4070 8GB, pantalla QHD+ 165Hz.",
            "precio": 6499.00,
            "stock": 8,
            "categoria": "Laptops",
            "disponible": True
        },
        {
            "nombre": "Laptop Dell XPS 15 9530",
            "descripcion": "Intel Core i7-13700H, 16GB RAM, 512GB SSD, Intel Arc A370M, pantalla táctil OLED 3.5K.",
            "precio": 5890.50,
            "stock": 5,
            "categoria": "Laptops",
            "disponible": True
        },
        {
            "nombre": "Monitor Gamer LG UltraGear 27''",
            "descripcion": "Resolución 2K QHD (2560x1440), panel Nano IPS 1ms, 165Hz, compatible con G-Sync y FreeSync Premium.",
            "precio": 1349.00,
            "stock": 14,
            "categoria": "Monitores",
            "disponible": True
        },
        {
            "nombre": "Monitor Samsung Odyssey G5 32''",
            "descripcion": "Curvatura 1000R, resolución WQHD 144Hz, tiempo de respuesta 1ms, HDR10.",
            "precio": 1199.90,
            "stock": 0,  # Sin stock intencional para verificar filtro {% if %}
            "categoria": "Monitores",
            "disponible": False
        },
        {
            "nombre": "Teclado Mecánico Keychron Q1 Pro",
            "descripcion": "Switches mecánicos lubricados Red, conectividad Bluetooth 5.1 y cable Type-C, chasis de aluminio CNC.",
            "precio": 749.00,
            "stock": 20,
            "categoria": "Periféricos",
            "disponible": True
        },
        {
            "nombre": "Mouse Logitech G Pro X Superlight 2",
            "descripcion": "Sensor HERO 2 de 32,000 DPI, peso ultraligero de 60g, interruptores Lightforce híbridos óptico-mecánicos.",
            "precio": 529.00,
            "stock": 18,
            "categoria": "Periféricos",
            "disponible": True
        },
        {
            "nombre": "Auriculares Sony WH-1000XM5",
            "descripcion": "Cancelación de ruido líder en la industria, sonido Hi-Res con codec LDAC, 30 horas de batería continua.",
            "precio": 1289.00,
            "stock": 9,
            "categoria": "Audio",
            "disponible": True
        },
        {
            "nombre": "Micrófono Shure MV7 USB/XLR",
            "descripcion": "Cápsula dinámica para podcasting y streaming profesional, salida dual USB/XLR y panel táctil.",
            "precio": 999.00,
            "stock": 6,
            "categoria": "Audio",
            "disponible": True
        },
        {
            "nombre": "Router Wi-Fi 6 ASUS RT-AX88U Pro",
            "descripcion": "Doble banda AX6000, puerto dual 2.5G, seguridad de red comercial AiProtection Pro gratuita.",
            "precio": 1050.00,
            "stock": 11,
            "categoria": "Redes",
            "disponible": True
        }
    ]

    print("\n[+] Insertando productos en SQLite mediante Producto.objects.create()...")
    creados = []
    for item in productos_data:
        p = Producto.objects.create(**item)
        creados.append(p)
        print(f"    - Creado ID [{p.id}]: {p.nombre} | S/. {p.precio:.2f} | Categoría: {p.categoria}")

    print(f"\n[OK] Se han registrado exitosamente {len(creados)} productos.")

    # Demostración de consultas ORM requeridas por la Guía Práctica
    print("\n" + "=" * 70)
    print("DEMOSTRACIÓN DE CONSULTAS ORM CON QUERYSETS:")
    print("=" * 70)

    # 1. objects.all()
    print("\n1. CONSULTA TOTAL CON Producto.objects.all():")
    todos = Producto.objects.all()
    print(f"   Total recuperado: {todos.count()} registros (Lazy Evaluation: {type(todos)})")
    for prod in todos[:3]:
        print(f"   * [ID: {prod.id}] {prod}")

    # 2. objects.filter(categoria='Laptops')
    print("\n2. CONSULTA FILTRADA POR CATEGORÍA: Producto.objects.filter(categoria='Laptops'):")
    laptops = Producto.objects.filter(categoria='Laptops')
    for lap in laptops:
        print(f"   * {lap.nombre} | Precio: S/. {lap.precio:.2f} | Stock: {lap.stock}")

    # 3. objects.filter(precio__gte=1000, disponible=True)
    print("\n3. CONSULTA CON LOOKUPS AVANZADOS: Producto.objects.filter(precio__gte=1000, disponible=True):")
    gama_alta = Producto.objects.filter(precio__gte=1000, disponible=True)
    for g in gama_alta:
        print(f"   * {g.nombre} -> S/. {g.precio:.2f} (Stock: {g.stock})")

    # 4. objects.filter(stock=0)
    print("\n4. CONSULTA DE PRODUCTOS AGOTADOS: Producto.objects.filter(stock=0):")
    agotados = Producto.objects.filter(stock=0)
    for ag in agotados:
        print(f"   * {ag.nombre} -> Estado disponible: {ag.disponible}")

    print("\n" + "=" * 70)
    print("POBLADO Y VERIFICACIÓN ORM FINALIZADOS EXITOSAMENTE")
    print("=" * 70)

if __name__ == '__main__':
    poblar_catalogo()
