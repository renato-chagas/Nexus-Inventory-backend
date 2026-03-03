#!/usr/bin/env python
import os
import sys
import django
from datetime import datetime, timedelta
import random

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
django.setup()

from core.nexus_inventory.models import Asset, AssetHistory, Category, Employee


def populate_database():
    # Pega uma categoria existente
    category = Category.objects.first()
    if not category:
        category = Category.objects.create(
            name="Equipamentos", description="Equipamentos em geral"
        )

    # Pega funcionários existentes
    employees = list(Employee.objects.all())
    if not employees:
        print("Nenhum funcionário encontrado!")
        return

    print(f"Criando 20 ativos com histórico...")

    assets_created = 0
    for i in range(20):
        # Cria ativo
        asset = Asset.objects.create(
            name=f"Equipamento {i+1}",
            category=category,
            specs=f"Especificações do equipamento {i+1}",
            serial_number=f"SN-2026-{i+1:04d}",
            status="IN_USE",
            bought_price=1000.00 + (i * 50),
            bought_date="2026-01-01",
            person_in_charge=random.choice(employees),
        )

        # Cria 2-3 históricos para cada ativo
        num_histories = random.randint(2, 3)
        action_types = ["CHECKOUT", "CHECKIN", "MAINTENANCE"]

        for h in range(num_histories):
            # Histórico com data regressiva
            days_ago = 30 - (h * 10)
            action_date = datetime.now() - timedelta(days=days_ago)

            AssetHistory.objects.create(
                asset=asset,
                employee=random.choice(employees),
                action_type=random.choice(action_types),
                action_date=action_date,
                observaitions=f"Histórico #{h+1} do equipamento {i+1}",
            )

        assets_created += 1
        print(f"✓ Ativo {i+1}/20 criado com {num_histories} históricos")

    print(f"\n✅ {assets_created} ativos criados com sucesso!")
    print(f"Total de ativos: {Asset.objects.count()}")
    print(f"Total de históricos: {AssetHistory.objects.count()}")


if __name__ == "__main__":
    populate_database()
