from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`ASSALAMUALAIKUM PARA JAMET..`")


@register(outgoing=True, pattern='^S(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`SOKAP BANGET LU KENAL KAGA MAEN REP REP AJA..!`")


@register(outgoing=True, pattern='^W(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`WAR WAR TAI ANJING!!! SOK SOK AN NANTANG WAR, EH KE TRIGGERED MINTA SHARE LOCK. PAS UDAH DI SHARE LOCK NGILANG. MENTAL KEK TAI.!!`")


@register(outgoing=True, pattern='^A(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Apaan Sih`")


@register(outgoing=True, pattern='^.pp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`PASANG PP DULU LU NGENTOT BIAR SEMUA ORANG TAU MUKA LU YANG HINA ITU CIIIHHHH.. `")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumssalam Wr. Wb. `")


@register(outgoing=True, pattern='^B(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`BANYAK BACOT LU GOBLOK `")


@register(outgoing=True, pattern='^Y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Yaudah Iyain Saja..`")


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`GAMAO LU BAUU TANAH KUBURAN...🥺`")


CMD_HELP.update({
    "salam":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.P`\
\n↳ : Untuk Memberi salam.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `G`\
\n↳ : Ngatain.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `A`\
\n↳ : Coba Aja Sendiri.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pp`\
\n↳ : Hina Yang Gapake PP.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `B`\
\n↳ : Buat Dikasih Ke Yang Banyak Bacot.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `W`\
\n↳ : Ngatain Anak Sok Ngewar.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `S`\
\n↳ : Ngatain Orang Sok Akrab.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Y`\
\n↳ : Kalo Debat Pake Aja.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.L`\
\n↳ : Untuk Menjawab Salam."
})
