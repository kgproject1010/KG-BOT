from time import sleep
from platform import uname
from userbot import ALIVE_NAME, WEATHER_DEFCITY, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG GOBLOKK!!!**")
# Pantun


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`HALO PARA JAMET`")
    sleep(2)
    await typew.edit("`ASSALAMUALAIKUM PARA PENGANGGURAN`")
# Salam


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`KALO ORANG SALAM ITU DIJAWAB TOLOL...`")
    sleep(2)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Menjawab Salam


@register(outgoing=True, pattern="^.kenalin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `Apis Gila`")
    sleep(2)
    await typew.edit("✅ `Apis Gila`")
    sleep(1)
    await typew.edit("☑️ `Skyzo Stress`")
    sleep(2)
    await typew.edit("✅ `Skyzo Stress`")
    sleep(1)
    await typew.edit("☑️ `Yunus Gajelas`")
    sleep(2)
    await typew.edit("✅ `Yunus Gajelas`")
    sleep(1)
    await typew.edit("☑️ `Tegar Wibu Sangean`")
    sleep(2)
    await typew.edit("✅ `Tegar Wibu Sangean`")
    sleep(1)
    await typew.edit("☑️ `Can Autis`")
    sleep(2)
    await typew.edit("✅ `Can Autis`")
    sleep(1)
    await typew.edit("`⚡ Cuma KG Yang Paling Waras, Baik Hati, Dan Tidak Sombong :v`")
# King Userbot Support


@register(outgoing=True, pattern="^.la(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `Piah Owner Sadis`")
    sleep(1)
    await typew.edit("✅ `Piah Owner Sadis`")
    sleep(2)
    await typew.edit("☑️ `Icah Gila`")
    sleep(1)
    await typew.edit("✅ `Icah Gila`")
    sleep(2)
    await typew.edit("☑️ `Kia Babi`")
    sleep(1)
    await typew.edit("✅ `Kia Babi`")
    sleep(2)
    await typew.edit("☑️ `Yan Bapak Pekerja Keras`")
    sleep(1)
    await typew.edit("✅ `Yan Bapak Pekerja Keras`")
    sleep(2)
    await typew.edit("☑️ `Bra Gaje`")
    sleep(1)
    await typew.edit("✅ `Bra Gaje`")
    sleep(2)
    await typew.edit("✨ `Cuma KG Yang Paling Sopan, Baik Hati, Dan Tidak Sombong :v`")
# Luar Angkasa


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`LO GABOLEH NGOMONG KASAR TOLOL..`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")
# Istigfar


@register(outgoing=True, pattern="^.perkenalan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")
# Perkenalan


CMD_HELP.update(
    {
        "gabut": "**Modules** - `Gabut`\
        \n\n Cmd : `.l`\
        \nUsage : Untuk Menjawab Salam\
        \n\n Cmd : `.perkenalan`\
        \nUsage : Memperkenalkan Diri\
        \n\n Cmd : `.la`\
        \nUsage : Luar Angkasa\
        \n\n Cmd : `.g`\
        \nUsage : Member Goblok\
        \n\n Cmd : `.kenalin`\
        \nUsage : Awokwok\
        \n\n Cmd : `.p`\
        \nUsage : Untuk Memberi Salam\
    "
    }
)
