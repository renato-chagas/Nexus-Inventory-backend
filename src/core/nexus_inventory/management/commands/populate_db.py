from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from decimal import Decimal

from core.nexus_inventory.models import (
    Category,
    Employee,
    Software,
    Asset,
    AssetHistory,
)


class Command(BaseCommand):
    help = "Populates the database with sample data for all models"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting database population..."))

        # Create Categories
        self.stdout.write("Creating categories...")
        categories = []
        category_data = [
            {
                "name": "Laptops",
                "tracks_software": True,
                "description": "Notebook computers for employees",
            },
            {
                "name": "Monitors",
                "tracks_software": False,
                "description": "Desktop monitors",
            },
            {
                "name": "Keyboards",
                "tracks_software": False,
                "description": "Computer keyboards",
            },
            {
                "name": "Mouses",
                "tracks_software": False,
                "description": "Computer mouses",
            },
            {
                "name": "Servers",
                "tracks_software": True,
                "description": "Server equipment",
            },
            {
                "name": "Printers",
                "tracks_software": False,
                "description": "Office printers",
            },
        ]

        for cat_data in category_data:
            category, created = Category.objects.get_or_create(
                name=cat_data["name"],
                defaults={
                    "tracks_software": cat_data["tracks_software"],
                    "description": cat_data["description"],
                },
            )
            categories.append(category)
            if created:
                self.stdout.write(f"  ✓ Created category: {category.name}")
            else:
                self.stdout.write(f"  ✓ Category already exists: {category.name}")

        # Create Employees
        self.stdout.write("Creating employees...")
        employees = []
        employee_data = [
            {
                "name": "João",
                "surname": "Silva",
                "email": "joao.silva@example.com",
                "phone": "11987654321",
                "department": "IT",
            },
            {
                "name": "Maria",
                "surname": "Santos",
                "email": "maria.santos@example.com",
                "phone": "11987654322",
                "department": "HR",
            },
            {
                "name": "Pedro",
                "surname": "Oliveira",
                "email": "pedro.oliveira@example.com",
                "phone": "11987654323",
                "department": "Finance",
            },
            {
                "name": "Ana",
                "surname": "Costa",
                "email": "ana.costa@example.com",
                "phone": "11987654324",
                "department": "IT",
            },
            {
                "name": "Carlos",
                "surname": "Ferreira",
                "email": "carlos.ferreira@example.com",
                "phone": "11987654325",
                "department": "Operations",
            },
        ]

        for emp_data in employee_data:
            employee, created = Employee.objects.get_or_create(
                email=emp_data["email"],
                defaults={
                    "name": emp_data["name"],
                    "surname": emp_data["surname"],
                    "phone": emp_data["phone"],
                    "department": emp_data["department"],
                },
            )
            employees.append(employee)
            if created:
                self.stdout.write(
                    f"  ✓ Created employee: {employee.name} {employee.surname}"
                )
            else:
                self.stdout.write(
                    f"  ✓ Employee already exists: {employee.name} {employee.surname}"
                )

        # Create Software
        self.stdout.write("Creating software...")
        software_list = []
        software_data = [
            {"name": "Windows", "version": "11"},
            {"name": "Windows", "version": "10"},
            {"name": "Microsoft Office", "version": "365"},
            {"name": "Adobe Creative Suite", "version": "2024"},
            {"name": "Visual Studio Code", "version": "1.96"},
            {"name": "Git", "version": "2.43"},
            {"name": "Python", "version": "3.12"},
            {"name": "Docker", "version": "25.0"},
            {"name": "Zoom", "version": "6.0"},
            {"name": "Slack", "version": "4.38"},
        ]

        for soft_data in software_data:
            software, created = Software.objects.get_or_create(
                name=soft_data["name"], version=soft_data["version"]
            )
            software_list.append(software)
            if created:
                self.stdout.write(
                    f"  ✓ Created software: {software.name} {software.version}"
                )
            else:
                self.stdout.write(
                    f"  ✓ Software already exists: {software.name} {software.version}"
                )

        # Create Assets
        self.stdout.write("Creating assets...")
        assets = []
        asset_data = [
            {
                "name": "Dell XPS 13",
                "category_name": "Laptops",
                "serial": "DELL-XPS-001",
                "status": "IN_USE",
                "bought_price": Decimal("5000.00"),
                "bought_date": (timezone.now() - timedelta(days=365)).date(),
                "person_in_charge": 0,
            },
            {
                "name": "MacBook Pro 16",
                "category_name": "Laptops",
                "serial": "MB-PRO-001",
                "status": "IN_USE",
                "bought_price": Decimal("6500.00"),
                "bought_date": (timezone.now() - timedelta(days=180)).date(),
                "person_in_charge": 1,
            },
            {
                "name": "HP Pavilion 15",
                "category_name": "Laptops",
                "serial": "HP-PAV-001",
                "status": "IN_USE",
                "bought_price": Decimal("3500.00"),
                "bought_date": (timezone.now() - timedelta(days=210)).date(),
                "person_in_charge": 2,
            },
            {
                "name": "Lenovo ThinkPad X1",
                "category_name": "Laptops",
                "serial": "LEN-TP-001",
                "status": "AVAILABLE",
                "bought_price": Decimal("4800.00"),
                "bought_date": (timezone.now() - timedelta(days=75)).date(),
                "person_in_charge": None,
            },
            {
                "name": "Asus VivoBook 15",
                "category_name": "Laptops",
                "serial": "ASUS-VB-001",
                "status": "IN_USE",
                "bought_price": Decimal("3200.00"),
                "bought_date": (timezone.now() - timedelta(days=120)).date(),
                "person_in_charge": 3,
            },
            {
                "name": 'LG Monitor 27"',
                "category_name": "Monitors",
                "serial": "LG-MON-001",
                "status": "AVAILABLE",
                "bought_price": Decimal("1200.00"),
                "bought_date": (timezone.now() - timedelta(days=90)).date(),
                "person_in_charge": None,
            },
            {
                "name": 'Dell Monitor 24"',
                "category_name": "Monitors",
                "serial": "DELL-MON-001",
                "status": "IN_USE",
                "bought_price": Decimal("800.00"),
                "bought_date": (timezone.now() - timedelta(days=150)).date(),
                "person_in_charge": 0,
            },
            {
                "name": 'Samsung Monitor 32"',
                "category_name": "Monitors",
                "serial": "SAM-MON-001",
                "status": "IN_USE",
                "bought_price": Decimal("1500.00"),
                "bought_date": (timezone.now() - timedelta(days=200)).date(),
                "person_in_charge": 1,
            },
            {
                "name": 'ASUS Monitor 27" Curved',
                "category_name": "Monitors",
                "serial": "ASUS-MON-001",
                "status": "MAINTENANCE",
                "bought_price": Decimal("1300.00"),
                "bought_date": (timezone.now() - timedelta(days=180)).date(),
                "person_in_charge": None,
            },
            {
                "name": "Mechanical Keyboard RGB",
                "category_name": "Keyboards",
                "serial": "KEY-RGB-001",
                "status": "IN_USE",
                "bought_price": Decimal("350.00"),
                "bought_date": (timezone.now() - timedelta(days=60)).date(),
                "person_in_charge": 2,
            },
            {
                "name": "Logitech KB920",
                "category_name": "Keyboards",
                "serial": "LOG-KB-001",
                "status": "AVAILABLE",
                "bought_price": Decimal("250.00"),
                "bought_date": (timezone.now() - timedelta(days=30)).date(),
                "person_in_charge": None,
            },
            {
                "name": "Apple Magic Keyboard",
                "category_name": "Keyboards",
                "serial": "APPLE-KEY-001",
                "status": "IN_USE",
                "bought_price": Decimal("400.00"),
                "bought_date": (timezone.now() - timedelta(days=100)).date(),
                "person_in_charge": 1,
            },
            {
                "name": "Logitech MX Master",
                "category_name": "Mouses",
                "serial": "MOUSE-MX-001",
                "status": "MAINTENANCE",
                "bought_price": Decimal("280.00"),
                "bought_date": (timezone.now() - timedelta(days=120)).date(),
                "person_in_charge": None,
            },
            {
                "name": "Razer DeathAdder",
                "category_name": "Mouses",
                "serial": "RAZ-MOUSE-001",
                "status": "IN_USE",
                "bought_price": Decimal("320.00"),
                "bought_date": (timezone.now() - timedelta(days=80)).date(),
                "person_in_charge": 3,
            },
            {
                "name": "Logitech M705",
                "category_name": "Mouses",
                "serial": "LOG-M705-001",
                "status": "AVAILABLE",
                "bought_price": Decimal("200.00"),
                "bought_date": (timezone.now() - timedelta(days=40)).date(),
                "person_in_charge": None,
            },
            {
                "name": "Dell Server PowerEdge R750",
                "category_name": "Servers",
                "serial": "DELL-SRV-001",
                "status": "IN_USE",
                "bought_price": Decimal("15000.00"),
                "bought_date": (timezone.now() - timedelta(days=730)).date(),
                "person_in_charge": 3,
            },
            {
                "name": "HP ProLiant DL380",
                "category_name": "Servers",
                "serial": "HP-SERV-001",
                "status": "IN_USE",
                "bought_price": Decimal("12000.00"),
                "bought_date": (timezone.now() - timedelta(days=550)).date(),
                "person_in_charge": 4,
            },
            {
                "name": "Lenovo ThinkServer",
                "category_name": "Servers",
                "serial": "LEN-SERV-001",
                "status": "AVAILABLE",
                "bought_price": Decimal("10000.00"),
                "bought_date": (timezone.now() - timedelta(days=300)).date(),
                "person_in_charge": None,
            },
            {
                "name": "HP LaserJet Pro",
                "category_name": "Printers",
                "serial": "HP-PRINT-001",
                "status": "AVAILABLE",
                "bought_price": Decimal("2000.00"),
                "bought_date": (timezone.now() - timedelta(days=45)).date(),
                "person_in_charge": None,
            },
            {
                "name": "Canon ImageRunner",
                "category_name": "Printers",
                "serial": "CAN-PRINT-001",
                "status": "IN_USE",
                "bought_price": Decimal("2500.00"),
                "bought_date": (timezone.now() - timedelta(days=90)).date(),
                "person_in_charge": 0,
            },
            {
                "name": "Xerox WorkCentre",
                "category_name": "Printers",
                "serial": "XER-PRINT-001",
                "status": "MAINTENANCE",
                "bought_price": Decimal("3000.00"),
                "bought_date": (timezone.now() - timedelta(days=200)).date(),
                "person_in_charge": None,
            },
        ]

        for asset_info in asset_data:
            category = Category.objects.get(name=asset_info["category_name"])
            person_in_charge = (
                employees[asset_info["person_in_charge"]]
                if asset_info["person_in_charge"] is not None
                else None
            )

            asset, created = Asset.objects.get_or_create(
                serial_number=asset_info["serial"],
                defaults={
                    "name": asset_info["name"],
                    "category": category,
                    "status": asset_info["status"],
                    "bought_price": asset_info["bought_price"],
                    "bought_date": asset_info["bought_date"],
                    "person_in_charge": person_in_charge,
                    "specs": f'Sample specifications for {asset_info["name"]}',
                },
            )
            assets.append(asset)

            # Add software to laptops and servers
            if category.tracks_software and created:
                if "Laptop" in asset_info["name"]:
                    asset.installed_software.set(
                        software_list[:5]
                    )  # Add first 5 software
                elif "Server" in asset_info["name"]:
                    asset.installed_software.set(
                        software_list[4:8]
                    )  # Add software for servers

            if created:
                self.stdout.write(f"  ✓ Created asset: {asset.name}")
            else:
                self.stdout.write(f"  ✓ Asset already exists: {asset.name}")

        # Create Asset History
        self.stdout.write("Creating asset history...")
        for asset in assets:
            for i in range(2):  # Create 2 history records per asset
                history, created = (
                    AssetHistory.objects.get_or_create(
                        asset=(
                            asset if hasattr(asset, "asset") else None
                        ),  # This needs checking
                        defaults={
                            "action_type": ["CHECKOUT", "CHECKIN", "MAINTENANCE"][i],
                            "employee": asset.person_in_charge or employees[0],
                            "observaitions": f"Sample history record for {asset.name}",
                        },
                    )
                    if hasattr(asset, "asset_history")
                    else None
                )

                if created and history:
                    self.stdout.write(f"  ✓ Created history for asset: {asset.name}")

        self.stdout.write(
            self.style.SUCCESS("✓ Database population completed successfully!")
        )
