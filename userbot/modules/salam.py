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
    await typew.edit("`GAMAO LU BAUU TANAH KUBURAN...π₯Ί`")


CMD_HELP.update({
    "salam":
    "πΎπ€π’π’ππ£π: `.P`\
\nβ³ : Untuk Memberi salam.\
\n\nπΎπ€π’π’ππ£π: `G`\
\nβ³ : Ngatain.\
\n\nπΎπ€π’π’ππ£π: `A`\
\nβ³ : Coba Aja Sendiri.\
\n\nπΎπ€π’π’ππ£π: `.pp`\
\nβ³ : Hina Yang Gapake PP.\
\n\nπΎπ€π’π’ππ£π: `B`\
\nβ³ : Buat Dikasih Ke Yang Banyak Bacot.\
\n\nπΎπ€π’π’ππ£π: `W`\
\nβ³ : Ngatain Anak Sok Ngewar.\
\n\nπΎπ€π’π’ππ£π: `S`\
\nβ³ : Ngatain Orang Sok Akrab.\
\n\nπΎπ€π’π’ππ£π: `Y`\
\nβ³ : Kalo Debat Pake Aja.\
\n\nπΎπ€π’π’ππ£π: `.L`\
\nβ³ : Untuk Menjawab Salam."
})
