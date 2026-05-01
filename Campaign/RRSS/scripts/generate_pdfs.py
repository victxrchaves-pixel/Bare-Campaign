"""
Bare Campaign — PDF Generator
Generates 4 PDFs: full overview + one per phase
All in Spanish with English copies
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.flowables import Flowable
import os

# ── Paths ──────────────────────────────────────────────────────────────────
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'PDFs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Fonts ──────────────────────────────────────────────────────────────────
try:
    pdfmetrics.registerFont(TTFont('SFBold',   '/Library/Fonts/SF-Pro-Display-Bold.otf'))
    pdfmetrics.registerFont(TTFont('SFSemi',   '/Library/Fonts/SF-Pro-Display-Semibold.otf'))
    pdfmetrics.registerFont(TTFont('SFMedium', '/Library/Fonts/SF-Pro-Display-Medium.otf'))
    pdfmetrics.registerFont(TTFont('SFReg',    '/Library/Fonts/SF-Pro-Display-Regular.otf'))
    pdfmetrics.registerFont(TTFont('SFLight',  '/Library/Fonts/SF-Pro-Display-Light.otf'))
    pdfmetrics.registerFont(TTFont('SFThin',   '/Library/Fonts/SF-Pro-Display-Thin.otf'))
    FONT_BOLD   = 'SFBold'
    FONT_SEMI   = 'SFSemi'
    FONT_MED    = 'SFMedium'
    FONT_REG    = 'SFReg'
    FONT_LIGHT  = 'SFLight'
    FONT_THIN   = 'SFThin'
except Exception:
    FONT_BOLD   = 'Helvetica-Bold'
    FONT_SEMI   = 'Helvetica-Bold'
    FONT_MED    = 'Helvetica'
    FONT_REG    = 'Helvetica'
    FONT_LIGHT  = 'Helvetica'
    FONT_THIN   = 'Helvetica'

# ── Colors ─────────────────────────────────────────────────────────────────
CREAM  = colors.HexColor('#FAFAFA')
BLACK  = colors.HexColor('#101010')
GRAY   = colors.HexColor('#888888')
LGRAY  = colors.HexColor('#DDDDDD')
DGRAY  = colors.HexColor('#333333')

# ── Page setup ─────────────────────────────────────────────────────────────
W, H   = A4
ML, MR = 20*mm, 20*mm
MT, MB = 20*mm, 20*mm

# ── Styles ─────────────────────────────────────────────────────────────────
def styles():
    return {
        'cover_title': ParagraphStyle('ct',
            fontName=FONT_BOLD, fontSize=52, leading=56,
            textColor=CREAM, spaceAfter=6),
        'cover_sub': ParagraphStyle('cs',
            fontName=FONT_LIGHT, fontSize=14, leading=18,
            textColor=CREAM, spaceAfter=4, tracking=2),
        'cover_meta': ParagraphStyle('cm',
            fontName=FONT_THIN, fontSize=10, leading=13,
            textColor=colors.HexColor('#999999'), spaceAfter=0),

        'section_label': ParagraphStyle('sl',
            fontName=FONT_LIGHT, fontSize=9, leading=12,
            textColor=GRAY, spaceBefore=28, spaceAfter=8,
            tracking=3),
        'h1': ParagraphStyle('h1',
            fontName=FONT_BOLD, fontSize=28, leading=32,
            textColor=BLACK, spaceBefore=0, spaceAfter=10),
        'h2': ParagraphStyle('h2',
            fontName=FONT_SEMI, fontSize=18, leading=22,
            textColor=BLACK, spaceBefore=16, spaceAfter=6),
        'h3': ParagraphStyle('h3',
            fontName=FONT_MED, fontSize=13, leading=17,
            textColor=BLACK, spaceBefore=12, spaceAfter=4),
        'body': ParagraphStyle('body',
            fontName=FONT_REG, fontSize=10, leading=16,
            textColor=DGRAY, spaceAfter=6),
        'body_light': ParagraphStyle('bl',
            fontName=FONT_LIGHT, fontSize=9.5, leading=15,
            textColor=GRAY, spaceAfter=4),
        'copy_label': ParagraphStyle('cpl',
            fontName=FONT_LIGHT, fontSize=8, leading=11,
            textColor=GRAY, spaceBefore=10, spaceAfter=4,
            tracking=2),
        'copy_en': ParagraphStyle('cen',
            fontName=FONT_BOLD, fontSize=14, leading=19,
            textColor=BLACK, spaceAfter=6),
        'copy_caption': ParagraphStyle('cc',
            fontName=FONT_LIGHT, fontSize=9, leading=14,
            textColor=GRAY, spaceAfter=8),
        'tag': ParagraphStyle('tag',
            fontName=FONT_LIGHT, fontSize=8, leading=11,
            textColor=GRAY, tracking=1),
        'phase_header': ParagraphStyle('ph',
            fontName=FONT_BOLD, fontSize=36, leading=40,
            textColor=CREAM, spaceAfter=8),
        'phase_sub': ParagraphStyle('ps',
            fontName=FONT_LIGHT, fontSize=12, leading=16,
            textColor=CREAM, spaceAfter=0),
        'kpi_num': ParagraphStyle('kn',
            fontName=FONT_BOLD, fontSize=32, leading=36,
            textColor=BLACK, spaceAfter=0),
        'kpi_label': ParagraphStyle('kl',
            fontName=FONT_LIGHT, fontSize=9, leading=13,
            textColor=GRAY, spaceAfter=0),
    }

S = styles()

# ── Custom flowables ────────────────────────────────────────────────────────
class CoverBlock(Flowable):
    def __init__(self, title, subtitle, meta_lines, w=None, h=120*mm):
        self.title, self.subtitle, self.meta_lines = title, subtitle, meta_lines
        self._w = w or (W - ML - MR)
        self._h = h
        Flowable.__init__(self)

    def wrap(self, aw, ah):
        return self._w, self._h

    def draw(self):
        c = self.canv
        c.setFillColor(BLACK)
        c.rect(0, 0, self._w, self._h, fill=1, stroke=0)
        # title
        c.setFillColor(CREAM)
        c.setFont(FONT_BOLD, 48)
        c.drawString(10*mm, self._h - 28*mm, self.title)
        # subtitle
        c.setFont(FONT_LIGHT, 13)
        c.setFillColor(colors.HexColor('#AAAAAA'))
        c.drawString(10*mm, self._h - 38*mm, self.subtitle)
        # line
        c.setStrokeColor(colors.HexColor('#333333'))
        c.setLineWidth(0.5)
        c.line(10*mm, self._h - 44*mm, self._w - 10*mm, self._h - 44*mm)
        # meta
        y = self._h - 52*mm
        c.setFont(FONT_THIN, 9)
        c.setFillColor(colors.HexColor('#666666'))
        for line in self.meta_lines:
            c.drawString(10*mm, y, line)
            y -= 5*mm


class PhaseBlock(Flowable):
    def __init__(self, number, title, subtitle, w=None, h=45*mm, bg=BLACK):
        self.number, self.title, self.subtitle = number, title, subtitle
        self._w = w or (W - ML - MR)
        self._h = h
        self._bg = bg
        Flowable.__init__(self)

    def wrap(self, aw, ah):
        return self._w, self._h

    def draw(self):
        c = self.canv
        c.setFillColor(self._bg)
        c.rect(0, 0, self._w, self._h, fill=1, stroke=0)
        c.setFillColor(colors.HexColor('#333333'))
        c.setFont(FONT_BOLD, 60)
        c.drawString(8*mm, 8*mm, self.number)
        c.setFillColor(CREAM)
        c.setFont(FONT_BOLD, 22)
        c.drawString(8*mm, self._h - 16*mm, self.title)
        c.setFont(FONT_LIGHT, 10)
        c.setFillColor(colors.HexColor('#AAAAAA'))
        c.drawString(8*mm, self._h - 24*mm, self.subtitle)


class PostBlock(Flowable):
    def __init__(self, num, type_label, headline, copy_lines,
                 caption, w=None, inverted=False):
        self.num = num
        self.type_label = type_label
        self.headline = headline
        self.copy_lines = copy_lines
        self.caption = caption
        self._w = w or (W - ML - MR)
        self._inverted = inverted
        Flowable.__init__(self)

    def wrap(self, aw, ah):
        # estimate height
        lines = len(self.copy_lines)
        self._h = (50 + lines * 14 + 40) * mm / 10 + 30*mm
        return self._w, self._h

    def draw(self):
        c = self.canv
        bg = BLACK if self._inverted else colors.HexColor('#F2F2F2')
        fg = CREAM if self._inverted else BLACK
        c.setFillColor(bg)
        c.rect(0, 0, self._w, self._h, fill=1, stroke=0)
        # post number + type
        c.setFont(FONT_LIGHT, 8)
        c.setFillColor(colors.HexColor('#666666') if self._inverted else GRAY)
        c.drawString(6*mm, self._h - 7*mm, f'POST {self.num}  ·  {self.type_label}')
        # separator
        c.setStrokeColor(colors.HexColor('#333333') if self._inverted else LGRAY)
        c.setLineWidth(0.4)
        c.line(6*mm, self._h - 10*mm, self._w - 6*mm, self._h - 10*mm)
        # headline
        c.setFillColor(fg)
        c.setFont(FONT_BOLD, 15)
        y = self._h - 19*mm
        c.drawString(6*mm, y, self.headline)
        # copy
        c.setFont(FONT_BOLD, 11)
        y -= 8*mm
        for line in self.copy_lines:
            if line == '—':
                c.setStrokeColor(colors.HexColor('#444444') if self._inverted else LGRAY)
                c.line(6*mm, y + 2*mm, self._w - 6*mm, y + 2*mm)
                y -= 5*mm
            else:
                c.setFillColor(fg)
                c.drawString(8*mm, y, line)
                y -= 5.5*mm
        # caption label
        y -= 4*mm
        c.setFont(FONT_LIGHT, 8)
        c.setFillColor(colors.HexColor('#666666'))
        c.drawString(6*mm, y, 'CAPTION')
        y -= 4.5*mm
        c.setFont(FONT_LIGHT, 8.5)
        c.setFillColor(colors.HexColor('#888888') if self._inverted else GRAY)
        for seg in self.caption.split('\n'):
            c.drawString(8*mm, y, seg[:90])
            y -= 4*mm


def hr(color=LGRAY, thickness=0.5):
    return HRFlowable(width='100%', thickness=thickness, color=color,
                      spaceAfter=6, spaceBefore=6)


def label(text):
    return Paragraph(text.upper(), S['section_label'])


def kpi_table(items):
    """items = [(number, label), ...]"""
    data = [[Paragraph(n, S['kpi_num']), Paragraph(l, S['kpi_label'])] for n, l in items]
    t = Table([[d[0] for d in data], [d[1] for d in data]],
              colWidths=[(W - ML - MR) / len(items)] * len(items))
    t.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, LGRAY),
    ]))
    return t


# ══════════════════════════════════════════════════════════════════════════════
# CONTENT DATA
# ══════════════════════════════════════════════════════════════════════════════

POSTS = {
    'brand': [
        {
            'num': '01', 'inverted': False,
            'type': 'IMAGEN SIMPLE',
            'headline': 'Bare. Coming Soon.',
            'copy': ['BARE.', 'COMING SOON.', '—', 'bare'],
            'caption': 'bare.\n\ncoming soon.',
            'desc': 'Primera aparición de la marca. Solo el nombre y el anuncio. Sin explicaciones.',
        },
        {
            'num': '02', 'inverted': True,
            'type': 'CARRUSEL 4 SLIDES',
            'headline': 'Not a Portfolio / Carousel',
            'copy': [
                'S1: NOT A PORTFOLIO.',
                'S2: NOT A MARKETPLACE.',
                'S3: NOT INSTAGRAM.',
                'S4 (fondo oscuro): bare.',
            ],
            'caption': 'not a portfolio.\nnot a marketplace.\nnot instagram.\n\nbare.\n\none platform for visual creators.\nwaitlist → link in bio',
            'desc': 'Carrusel de 4 slides. Cada línea en su propio slide en fondo claro. El slide 4 invierte a fondo #101010 con solo "bare." centrado — el remate de la secuencia.',
        },
        {
            'num': '03', 'inverted': False,
            'type': 'IMAGEN SIMPLE — TEASER UI',
            'headline': 'Teaser UI: Buscador vacío',
            'copy': [
                'FILTER BY PALETTE.',
                'BY TECHNIQUE.',
                'BY ATMOSPHERE.',
                '—',
                'bare',
            ],
            'caption': 'search by what the work looks like.\nnot by who made it.\n\npalette. technique. atmosphere.\nthat\'s how bare works.\n\ncoming soon. waitlist → link in bio',
            'desc': 'Captura del buscador vacío de Bare (sin usuarios), convertida a blanco y negro. El copy se superpone en el tercio inferior sobre la pantalla.',
        },
    ],
    'waitlist': [
        {
            'num': '04', 'inverted': False,
            'type': 'CARRUSEL 7 SLIDES',
            'headline': 'What is Bare — Explicación completa',
            'copy': [
                'S1 (oscuro): WHAT IS BARE AND HOW ACCESS WORKS.',
                'S2: BARE IS A PLATFORM FOR VISUAL CREATORS.',
                'S3: IT\'S NOT OPEN.',
                'S4: WHAT DO WE EVALUATE?',
                'S5: ONCE INSIDE...',
                'S6 (oscuro): SEARCH WORKS DIFFERENTLY HERE.',
                'S7 (oscuro): WAITLIST OPEN. 30 SPOTS THIS WEEK.',
            ],
            'caption': 'what is bare — and how does access work?\n\narchive. portfolio. network. one place.\nyou submit a project. a team reviews it.\nyou\'re in or you\'re not.\n\nwaitlist open. 30 spots this week.\nlink in bio.',
            'desc': 'El carrusel principal de explicación. 7 slides que cuentan qué es Bare, cómo funciona el acceso, qué se evalúa y qué hay dentro. Termina con CTA de waitlist.',
        },
        {
            'num': '05', 'inverted': False,
            'type': 'IMAGEN SIMPLE — FOMO',
            'headline': '30 Spots This Week',
            'copy': [
                '30',
                'SPOTS',
                'THIS WEEK.',
                '—',
                'BATCH [N] · CLOSES SUNDAY.',
                'bare · waitlist in bio',
            ],
            'caption': 'batch [n] open.\n\n30 spots this week.\ncloses sunday.\n\nlink in bio → bare waitlist',
            'desc': 'Template reutilizable cada semana. El "30" ocupa casi todo el frame. Actualizar [N] con número de lote real. Puede reusarse 4 veces durante el Mes 2.',
        },
        {
            'num': '06', 'inverted': False,
            'type': 'IMAGEN SIMPLE — CONTRASTE',
            'headline': 'You Have 4 Tabs Open',
            'copy': [
                'YOU HAVE 4 TABS',
                'OPEN WHILE TRYING',
                'TO CREATE.',
                '—',
                'BARE IS ONE.',
                'bare · waitlist in bio',
            ],
            'caption': 'you have 4 tabs open while trying to create.\npinterest. behance. instagram. linkedin.\n\nbare is one.\n\nwaitlist open → link in bio',
            'desc': 'El problema del creador como telón de fondo. Usar una sola vez en el Mes 2. El peso tipográfico del problema (Regular) vs. la solución (SemiBold) es intencional.',
        },
    ],
    'closing': [
        {
            'num': '07', 'inverted': True,
            'type': 'IMAGEN SIMPLE — URGENCIA',
            'headline': '[X] Spots Left',
            'copy': [
                '[X]',
                'SPOTS LEFT.',
                '—',
                'BARE LAUNCHES [DATE].',
                'bare · waitlist in bio',
            ],
            'caption': '[x] spots left.\n\nbare launches [date].\nthe waitlist closes before that.\n\nlink in bio.',
            'desc': 'Fondo #101010. El número real de plazas restantes ocupa el centro del frame. Publicar múltiples veces actualizando [X] con el conteo real. Sin hashtags.',
        },
        {
            'num': '08', 'inverted': False,
            'type': 'CARRUSEL 5 SLIDES',
            'headline': 'From 0 to 200 — Journey',
            'copy': [
                'S1: FROM 0 TO 200.',
                'S2: 50 — The first creators who believed.',
                'S3: 100 — Halfway. The filter worked.',
                'S4: 150 — 50 spots left. This is where it gets real.',
                'S5 (oscuro): 200. WAITLIST CLOSES [DATE]. [X] SPOTS LEFT.',
            ],
            'caption': '50. then 100. then 150.\n\nnow [x] spots left before we close.\n\nbare launches [date].\nwaitlist closes before that.\n\nlink in bio.',
            'desc': 'Carrusel de recapitulación. Cuenta el journey de los hitos antes del cierre. Slide 5 invierte a fondo oscuro. El número domina cada slide con texto pequeño debajo.',
        },
        {
            'num': '09', 'inverted': False,
            'type': 'IMAGEN SIMPLE — CIERRE OFICIAL',
            'headline': 'Waitlist Closed',
            'copy': [
                'WAITLIST',
                'CLOSED.',
                '—',
                '200 CREATORS INSIDE.',
                'BARE LAUNCHES [DATE].',
                '—',
                'bare',
            ],
            'caption': 'waitlist closed.\n\n200 creators inside.\nbare launches [date].\n\nthank you.',
            'desc': 'Vuelve al fondo claro #FAFAFA después de la fase oscura de urgencia. Sin CTA. Solo el anuncio limpio. Publicar solo el día del cierre de la waitlist.',
        },
    ],
}

IDENTITY = {
    'palette': [
        ('Principal', '#FAFAFA', 'Blanco roto — base de todas las piezas'),
        ('Secundario', '#101010', 'Negro casi puro — texto y elementos dominantes'),
        ('Inversión', '#101010 bg / #FAFAFA text', 'Solo en urgencia (Mes 3) y TikTok'),
    ],
    'typography': [
        ('Titulares', 'Switzer', 'Regular, Medium o SemiBold · MAYÚSCULAS'),
        ('Cuerpo / firma', 'Geist', 'Regular o Light · "bare" siempre en minúscula'),
    ],
    'formats': [
        ('IG Feed cuadrado', '1080 × 1080 px', 'Posts de manifiesto e hitos'),
        ('IG Feed vertical', '1080 × 1350 px', 'Posts con más texto o carrusel'),
        ('IG Stories / TK', '1080 × 1920 px', 'Stories diarias y vídeos TikTok'),
    ],
}

# ══════════════════════════════════════════════════════════════════════════════
# BUILDERS
# ══════════════════════════════════════════════════════════════════════════════

def build_overview():
    path = os.path.join(OUTPUT_DIR, 'Bare_Campaña_Completa.pdf')
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=ML, rightMargin=MR,
                            topMargin=MT, bottomMargin=MB)
    story = []

    # ── Cover ──────────────────────────────────────────────────────────────
    story.append(CoverBlock(
        title='BARE',
        subtitle='Campaña de prelanzamiento — Visión completa',
        meta_lines=[
            'INSTAGRAM + TIKTOK   ·   3 MESES   ·   200 PERSONAS EN WAITLIST',
            'TONO: MANIFIESTO / BOLD   ·   PALETA: #FAFAFA / #101010',
            'TIPOGRAFÍA: SWITZER (TITULARES) + GEIST (CUERPO)',
            'TODOS LOS COPIES EN INGLÉS',
        ],
        h=80*mm,
    ))
    story.append(Spacer(1, 10*mm))

    # ── Intro ──────────────────────────────────────────────────────────────
    story.append(label('¿Qué es bare?'))
    story.append(Paragraph('Bare es una plataforma para creadores visuales que unifica archivo de inspiración, portfolio profesional y directorio de contacto en un solo lugar. El acceso es restringido: se envía un proyecto, lo revisa un equipo humano, entras o no. La visibilidad se gana por la calidad del trabajo, no por el engagement ni por la capacidad de pago.', S['body']))
    story.append(Spacer(1, 4*mm))

    # ── Objetivo ───────────────────────────────────────────────────────────
    story.append(label('Objetivo de la campaña'))
    story.append(kpi_table([
        ('200', 'personas en waitlist'),
        ('3', 'meses de campaña'),
        ('2', 'plataformas: IG + TK'),
        ('9', 'posts principales'),
    ]))
    story.append(Spacer(1, 6*mm))

    # ── Estrategia ─────────────────────────────────────────────────────────
    story.append(label('Estrategia'))
    story.append(Paragraph('El eje central de la campaña es <b>lo que Bare ofrece</b>, no el problema del creador. El problema aparece como contraste puntual, máximo dos veces en todo el Mes 2. El FOMO es real: la waitlist abre en lotes semanales de 30 plazas. Cuando se agotan, se cierran hasta la semana siguiente. La escasez nunca es fabricada — siempre son números reales.', S['body']))
    story.append(Spacer(1, 4*mm))

    # ── Fases overview ─────────────────────────────────────────────────────
    story.append(label('Las 3 fases'))

    phases = [
        ('01', 'MARCA', 'Semanas 1–4', 'Construir reconocimiento de marca antes de pedir nada. Solo identidad. Sin CTA de waitlist. Sin revelar funcionalidades completas.'),
        ('02', 'WAITLIST', 'Semanas 5–8', 'Revelar qué es Bare y abrir la waitlist en lotes de 30 plazas por semana. El problema aparece puntualmente como contraste.'),
        ('03', 'CIERRE', 'Semanas 9–12', 'Countdown real. Plazas restantes visibles. La waitlist se cierra 1–2 semanas antes del lanzamiento. Los que no estén dentro, esperan.'),
    ]
    for num, title, weeks, desc in phases:
        story.append(KeepTogether([
            PhaseBlock(num, title, weeks, h=30*mm),
            Spacer(1, 2*mm),
            Paragraph(desc, S['body']),
            Spacer(1, 3*mm),
        ]))

    story.append(Spacer(1, 4*mm))

    # ── Identidad visual ───────────────────────────────────────────────────
    story.append(label('Identidad visual'))
    story.append(Paragraph('<b>Paleta de color</b>', S['h3']))
    for name, val, desc in IDENTITY['palette']:
        story.append(Paragraph(f'<b>{name}:</b> {val} — {desc}', S['body']))

    story.append(Paragraph('<b>Tipografía</b>', S['h3']))
    for role, font, specs in IDENTITY['typography']:
        story.append(Paragraph(f'<b>{role}:</b> {font} · {specs}', S['body']))

    story.append(Paragraph('<b>Formatos</b>', S['h3']))
    for fmt, size, use in IDENTITY['formats']:
        story.append(Paragraph(f'<b>{fmt}:</b> {size} — {use}', S['body']))

    story.append(Spacer(1, 4*mm))

    # ── 5 Pilares ──────────────────────────────────────────────────────────
    story.append(label('5 pilares de contenido'))
    pilares = [
        ('01 Manifiesto', 'Declaraciones en Switzer SemiBold. Identidad pura. Activo en Mes 1 y Mes 3.'),
        ('02 Teaser UI', 'Pantallas de la app en B&N con copy superpuesto. Genera deseo del producto. Mes 1 y Mes 3.'),
        ('03 Explicativo', 'Cómo funciona Bare: revisión humana, buscador, archivo. Carrusel IG + vídeo TK. Mes 2.'),
        ('04 FOMO / Escasez', 'Plazas disponibles, countdown, números reales. Activo desde la semana 5.'),
        ('05 Contraste', 'El problema del creador como telón. Máximo 2 veces en todo Mes 2.'),
    ]
    for title, desc in pilares:
        story.append(Paragraph(f'<b>{title}</b> — {desc}', S['body']))

    story.append(Spacer(1, 4*mm))

    # ── Los 9 posts ────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(label('Los 9 posts'))
    story.append(Paragraph('Resumen visual de todos los posts de la campaña. El copy aparece en inglés tal como se publicará.', S['body_light']))
    story.append(Spacer(1, 4*mm))

    for phase_key, phase_label in [('brand', 'FASE 1 — MARCA'), ('waitlist', 'FASE 2 — WAITLIST'), ('closing', 'FASE 3 — CIERRE')]:
        story.append(Paragraph(phase_label, S['section_label']))
        for p in POSTS[phase_key]:
            story.append(PostBlock(
                num=p['num'], type_label=p['type'],
                headline=p['headline'], copy_lines=p['copy'],
                caption=p['caption'], inverted=p['inverted'],
            ))
            story.append(Spacer(1, 3*mm))

    # ── Métricas ───────────────────────────────────────────────────────────
    story.append(PageBreak())
    story.append(label('Métricas objetivo'))
    metrics = [
        ('Waitlist total al cierre', '200 personas'),
        ('Seguidores IG al cierre', '+1.000 desde inicio'),
        ('Seguidores TK al cierre', '+500 desde inicio'),
        ('Lotes agotados en < 72h (Mes 2)', '3 de 4 lotes'),
        ('Engagement rate IG objetivo', '> 4%'),
        ('Engagement rate TK objetivo', '> 6%'),
    ]
    for label_m, val_m in metrics:
        story.append(Paragraph(f'<b>{label_m}:</b> {val_m}', S['body']))

    story.append(Spacer(1, 6*mm))
    story.append(label('Prerequisitos antes de publicar'))
    prereqs = [
        'Mockups de UI de las 4 pantallas listos y en blanco y negro',
        'Landing page / formulario de waitlist operativo (antes de la semana 5)',
        'Sistema de gestión de plazas configurado para conteo en tiempo real',
        'Cuentas IG y TK creadas con bio y link en bio activos',
        'Fecha de lanzamiento aproximada confirmada (necesaria desde el Mes 3)',
        'Persona asignada para actualizar Stories de countdown diariamente en Mes 3',
    ]
    for p in prereqs:
        story.append(Paragraph(f'— {p}', S['body']))

    doc.build(story)
    print(f'✓ {path}')


def build_phase(phase_key, phase_num, phase_title, phase_subtitle, weeks, objective, mechanics):
    filename = f'Bare_Fase{phase_num}_{phase_title}.pdf'
    path = os.path.join(OUTPUT_DIR, filename)
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=ML, rightMargin=MR,
                            topMargin=MT, bottomMargin=MB)
    story = []

    # Cover
    story.append(CoverBlock(
        title=f'FASE {phase_num} — {phase_title.upper()}',
        subtitle=f'{weeks}  ·  {phase_subtitle}',
        meta_lines=[
            'BARE — CAMPAÑA DE PRELANZAMIENTO',
            'INSTAGRAM + TIKTOK',
            'TODOS LOS COPIES EN INGLÉS',
        ],
        h=70*mm,
    ))
    story.append(Spacer(1, 8*mm))

    # Objetivo
    story.append(label('Objetivo de la fase'))
    story.append(Paragraph(objective, S['body']))
    story.append(Spacer(1, 3*mm))

    # Mecánica
    story.append(label('Mecánica y reglas'))
    for line in mechanics:
        story.append(Paragraph(f'— {line}', S['body']))
    story.append(Spacer(1, 5*mm))

    # Pilares activos
    pilares_map = {
        'brand':   '01 Manifiesto  ·  02 Teaser UI',
        'waitlist':'03 Explicativo  ·  04 FOMO / Escasez  ·  05 Contraste (máx. 2 veces)',
        'closing': '01 Manifiesto (Block B)  ·  02 Teaser UI  ·  04 FOMO / Escasez',
    }
    story.append(label('Pilares activos'))
    story.append(Paragraph(pilares_map[phase_key], S['body']))
    story.append(Spacer(1, 5*mm))

    # Los 3 posts
    story.append(label('Los 3 posts'))
    for p in POSTS[phase_key]:
        story.append(KeepTogether([
            Paragraph(f'POST {p["num"]} — {p["type"]}', S['h2']),
            Paragraph(p['desc'], S['body']),
            Spacer(1, 2*mm),
            Paragraph('COPY (EN INGLÉS)', S['copy_label']),
        ]))
        for line in p['copy']:
            story.append(Paragraph(line, S['copy_en']))
        story.append(Spacer(1, 2*mm))
        story.append(Paragraph('CAPTION DE INSTAGRAM', S['copy_label']))
        story.append(Paragraph(p['caption'].replace('\n', '<br/>'), S['copy_caption']))
        story.append(hr())
        story.append(Spacer(1, 4*mm))

    doc.build(story)
    print(f'✓ {path}')


# ══════════════════════════════════════════════════════════════════════════════
# RUN
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print('Generando PDFs...')

    build_overview()

    build_phase(
        'brand', '1', 'Marca', 'Construir reconocimiento antes de pedir nada',
        'Semanas 1–4',
        'Establecer la identidad de Bare antes de revelar funcionalidades o abrir la waitlist. Todo el contenido de esta fase es de identidad pura. Sin CTA de waitlist. Sin explicar qué hace la app. Solo que existe y que tiene un nivel.',
        [
            'Sin CTA de waitlist — ningún post de esta fase pide que la gente se apunte',
            'Sin revelar funcionalidades — el buscador, el archivo y el portfolio no se explican todavía',
            'El Teaser UI muestra pantallas vacías — la arquitectura, no el contenido',
            'La paleta es #FAFAFA en todas las piezas excepto el slide final del Post 02',
            'Frecuencia sugerida: 3–4 posts por semana + Stories diarias de identidad',
        ],
    )

    build_phase(
        'waitlist', '2', 'Waitlist', 'Revelar Bare y abrir la waitlist en lotes',
        'Semanas 5–8',
        'Revelar qué es Bare, cómo funciona el acceso y abrir la waitlist en lotes semanales de 30 plazas. Objetivo: 120 personas apuntadas al final de esta fase. Cuando un lote se agota, se cierra hasta la semana siguiente. Los números son siempre reales.',
        [
            'Waitlist abre el lunes de la semana 5 — anunciar con Story el domingo anterior',
            'Lotes de 30 plazas por semana — cuando se agotan, se cierran (sin rollover)',
            'Conteo de plazas en tiempo real en Stories de mitad de semana y cierre',
            'Post de contraste (Post 06): publicar solo una vez, en la semana 6',
            'Frecuencia: 4 posts por semana + Story de apertura/mid-week/cierre de lote',
        ],
    )

    build_phase(
        'closing', '3', 'Cierre', 'Countdown real y cierre de waitlist antes del lanzamiento',
        'Semanas 9–12',
        'Completar las 200 plazas y cerrar la waitlist 1–2 semanas antes del lanzamiento. El tono es sobrio y directo — nunca agresivo ni "última oportunidad". Las Stories pasan a ser diarias desde la semana 10 con días y plazas restantes en tiempo real.',
        [
            'Stories diarias desde semana 10 — días restantes + plazas disponibles, siempre reales',
            'Máximo 1 post de urgencia en feed cada 3 días — no saturar',
            'Fondo oscuro (#101010) como base de esta fase — señal visual de urgencia',
            'El día del cierre: un solo post limpio, sin celebración excesiva, sin hashtags',
            'Post 09 vuelve a fondo claro (#FAFAFA) — el cierre es un exhale, no un grito',
            'Confirmar la fecha de lanzamiento real antes de la semana 9',
        ],
    )

    print('\n✓ 4 PDFs generados en Campaign/RRSS/PDFs/')
