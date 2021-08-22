""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.ghelp$")
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/knsgnwn)"
        "\n[Repo](https://github.com/rakaanjay/KG-BOT)"
        "\n[Group](t.me/KGSupportgroup._)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/KennedyProject/KEN-UBOT/KEN-UBOT/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "`.ghelp`\
\nUsage: Bantuan Untuk KG-UBOT.\
\n`.vars`\
\nUsage: Melihat Daftar Vars."
})
