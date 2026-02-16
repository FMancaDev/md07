from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana: int):
        # Inicializa a parte 'Card'
        super().__init__(name, cost, rarity)
        # Atributos especificos das interfaces
        self.attack_power = attack
        self.health = health
        self.mana = mana
        self.max_health = health

    # --- Implementacao de Card ---
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite Summon: Enters ready for combat and magic"
        }

    # --- Implementacao de Combatable ---
    def attack(self, target) -> dict:
        # Simula o ataque. Target aqui e apenas uma string ou obj simulado
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = incoming_damage
        # Logica simples de defesa
        self.health -= damage_taken
        if self.health < 0:
            self.health = 0

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": 0,  # Simplificado conforme exemplo
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health,
            "max_health": self.max_health
        }

    # --- Implementacao de Magical ---
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        # Custo fixo simulado para exemplo
        mana_cost = 4
        if self.mana >= mana_cost:
            self.mana -= mana_cost
        else:
            return {"error": "Not enough mana"}

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "current_mana": self.mana,
            "spell_power_bonus": 0
        }
