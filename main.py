"""Script d'entraînement pour prendre en main Git et PEP 8."""

def calculer_rendement(prix_achat: float, prix_vente: float) -> float:
    """
    Calcule le rendement en pourcentage entre deux prix.
    Args:
      prix_achat: Le prix d'acquisition de l'action. 
      prix_vente: Le prix de revente de l'action. 
      
    Returns:
        Le rendement sous forme de pourcentage. 
    """
    return ((prix_vente - prix_achat) / prix_achat) * 100


def main() -> None: 
    """Affiche un message de bienvenue et teste la fonction de calcul.""" 
    print("Hello Git et GitHub !") 
    rendement = calculer_rendement(100.0, 115.0) 
    print(f"Rendement simulé : {rendement:.2f}%") 
    

if __name__ == "__main__": 
    main()