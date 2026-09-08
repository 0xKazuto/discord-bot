# Discord Bot 🤖

Un Discord bot en Python avec un système de commandes slash utilisant discord.py.

## Fonctionnalités

- ✅ Commandes slash (`/command`)
- ✅ Ping & Pong
- ✅ Répétition de messages
- ✅ Informations utilisateur
- ✅ Système d'aide
- ✅ Extensible et facile à modifier

## Commandes disponibles

| Commande | Description |
|----------|-------------|
| `/ping` | Retourne la latence du bot |
| `/say [message]` | Fait répéter le bot |
| `/user` | Affiche tes informations |
| `/hello` | Salue l'utilisateur |
| `/help` | Affiche l'aide du bot |

## Installation

### 1. Cloner le repository

```bash
git clone https://github.com/0xKazuto/discord-bot.git
cd discord-bot
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
```

### 3. Activer l'environnement virtuel

**Sur Windows:**
```bash
venv\Scripts\activate
```

**Sur macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 5. Configurer le token Discord

1. Copier `.env.example` en `.env`:
```bash
cp .env.example .env
```

2. Remplacer `your_bot_token_here` par votre token Discord

### 6. Lancer le bot

```bash
python bot.py
```

## Créer un Discord Bot

1. Aller sur [Discord Developer Portal](https://discord.com/developers/applications)
2. Cliquer sur "New Application"
3. Aller dans l'onglet "Bot" et cliquer "Add Bot"
4. Copier le token et le coller dans `.env`
5. Dans "OAuth2" → "URL Generator":
   - Sélectionner les scopes: `bot`
   - Sélectionner les permissions: `Send Messages`, `Read Messages/View Channels`, `Embed Links`
   - Copier l'URL générée et l'ouvrir pour inviter le bot

## Ajouter des commandes

C'est très simple ! Voici un exemple:

```python
@bot.tree.command(name='exemple', description='Une commande exemple')
async def exemple(interaction: discord.Interaction):
    await interaction.response.send_message('Coucou!')
```

## Structure du projet

```
discord-bot/
├── bot.py           # Code principal du bot
├── requirements.txt # Dépendances Python
├── .env.example     # Exemple de configuration
├── .gitignore       # Fichiers à ignorer
└── README.md        # Ce fichier
```

## Dépannage

### Le bot ne répond pas aux commandes
- Vérifiez que le token est correct
- Vérifiez que le bot a les permissions requises
- Redémarrez le bot

### Erreur "DISCORD_TOKEN non trouvé"
- Créez un fichier `.env` avec votre token
- Vérifiez que le fichier est nommé correctement

## Ressources

- [Discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Python Documentation](https://docs.python.org/3/)

## Licence

MIT License

## Auteur

0xKazuto