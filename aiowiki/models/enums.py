from enum import Enum


class Project(Enum):
    WIKIPEDIA = "wikipedia"
    # WIKTIONARY = "wiktionary"
    # WIKIQUOTE = "wikiquote"
    # WIKIVOYAGE = "wikivoyage"
    # WIKIBOOKS = "wikibooks"
    # WIKISOURCE = "wikisource"
    # WIKIVERSITY = "wikiversity"
    # COMMONS = "commons"
    # WIKISPECIES = "wikispecies"


class EventType(Enum):
    ALL = "all"
    SELECTED = "selected"
    BIRTHS = "births"
    DEATHS = "deaths"
    HOLIDAYS = "holidays"
    EVENTS = "events"


class LanguageDirection(Enum):
    LTR = "ltr"
    RTL = "rtl"


class PlatformType(Enum):
    DESKTOP = "desktop"
    MOBILE = "mobile"


class ArticleType(Enum):
    STANDARD = "standard"
    "Encyclopedia article"
    DISAMBIGUATION = "disambiguation"
    "Page that links to articles covering topics with similar titles"
    NO_EXTRACT = "no-extract"
    "Articles without an extract"
    MAINPAGE = "mainpage"
    "A wiki's homepage"


class MediaType(Enum):
    BITMAP = "BITMAP"
    DRAWING = "DRAWING"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    MULTIMEDIA = "MULTIMEDIA"
    UNKNOWN = "UNKNOWN"
    OFFICE = "OFFICE"
    TEXT = "TEXT"
    EXECUTABLE = "EXECUTABLE"
    ARCHIVE = "ARCHIVE"
    _3D = "3D"


class Language(Enum):
    ABKHAZIAN = "ab"
    AFAR = "aa"
    AFRIKAANS = "af"
    AKAN = "ak"
    ALBANIAN = "sq"
    AMHARIC = "am"
    ARABIC = "ar"
    ARAGONESE = "an"
    ARMENIAN = "hy"
    ASSAMESE = "as"
    AVARIC = "av"
    AVESTAN = "ae"
    AYMARA = "ay"
    AZERBAIJANI = "az"
    BAMBARA = "bm"
    BASHKIR = "ba"
    BASQUE = "eu"
    BELARUSIAN = "be"
    BENGALI = "bn"
    BISLAMA = "bi"
    BOSNIAN = "bs"
    BRETON = "br"
    BULGARIAN = "bg"
    BURMESE = "my"
    CATALAN = "al"
    CHAMORRO = "ch"
    CHECHEN = "ce"
    CHICHEWA = "he"
    CHINESE = "zh"
    CHURCH = "la"
    CHUVASH = "cv"
    CORNISH = "kw"
    CORSICAN = "co"
    CREE = "cr"
    CROATIAN = "hr"
    CZECH = "cs"
    DANISH = "da"
    DIVEHI = "hi"
    DUTCH = "le"
    DZONGKHA = "dz"
    ENGLISH = "en"
    ESPERANTO = "eo"
    ESTONIAN = "et"
    EWE = "ee"
    FAROESE = "fo"
    FIJIAN = "fj"
    FINNISH = "fi"
    FRENCH = "fr"
    WESTERN = "ri"
    FULAH = "ff"
    GAELIC = "co"
    GALICIAN = "gl"
    GANDA = "lg"
    GEORGIAN = "ka"
    GERMAN = "de"
    GREEK = "od"
    KALAALLISUT = "re"
    GUARANI = "gn"
    GUJARATI = "gu"
    HAITIAN = "ai"
    HAUSA = "ha"
    HEBREW = "he"
    HERERO = "hz"
    HINDI = "hi"
    HIRI = "ot"
    HUNGARIAN = "hu"
    ICELANDIC = "is"
    IDO = "io"
    IGBO = "ig"
    INDONESIAN = "id"
    INTERLINGUA = "nt"
    INTERLINGUE = "cc"
    INUKTITUT = "iu"
    INUPIAQ = "ik"
    IRISH = "ga"
    ITALIAN = "it"
    JAPANESE = "ja"
    JAVANESE = "jv"
    KANNADA = "kn"
    KANURI = "kr"
    KASHMIRI = "ks"
    KAZAKH = "kk"
    CENTRAL = "hm"
    KIKUYU = "ik"
    KINYARWANDA = "rw"
    KIRGHIZ = "yr"
    KOMI = "kv"
    KONGO = "kg"
    KOREAN = "ko"
    KUANYAMA = "wa"
    KURDISH = "ku"
    LAO = "lo"
    LATIN = "la"
    LATVIAN = "lv"
    LIMBURGAN = "im"
    LINGALA = "ln"
    LITHUANIAN = "lt"
    LUXEMBOURGISH = "et"
    MACEDONIAN = "mk"
    MALAGASY = "mg"
    MALAY = "ms"
    MALAYALAM = "ml"
    MALTESE = "mt"
    MANX = "gv"
    MAORI = "mi"
    MARATHI = "mr"
    MARSHALLESE = "mh"
    MONGOLIAN = "mn"
    NAURU = "na"
    NAVAJO = "av"
    NORTH = "de"
    SOUTH = "de"
    NDONGA = "ng"
    NEPALI = "ne"
    NORWEGIAN = "no"
    SICHUAN = "uo"
    OCCITAN = "oc"
    OJIBWA = "oj"
    ORIYA = "or"
    OROMO = "om"
    OSSETIAN = "ss"
    PALI = "pi"
    PASHTO = "us"
    PERSIAN = "fa"
    POLISH = "pl"
    PORTUGUESE = "pt"
    PUNJABI = "an"
    QUECHUA = "qu"
    ROMANIAN = "ol"
    ROMANSH = "rm"
    RUNDI = "rn"
    RUSSIAN = "ru"
    NORTHERN = "am"
    SAMOAN = "sm"
    SANGO = "sg"
    SANSKRIT = "sa"
    SARDINIAN = "sc"
    SERBIAN = "sr"
    SHONA = "sn"
    SINDHI = "sd"
    SINHALA = "in"
    SLOVAK = "sk"
    SLOVENIAN = "sl"
    SOMALI = "so"
    SOUTHERN = "ot"
    SPANISH = "as"
    SUNDANESE = "su"
    SWAHILI = "sw"
    SWATI = "ss"
    SWEDISH = "sv"
    TAGALOG = "tl"
    TAHITIAN = "ty"
    TAJIK = "tg"
    TAMIL = "ta"
    TATAR = "tt"
    TELUGU = "te"
    THAI = "th"
    TIBETAN = "bo"
    TIGRINYA = "ti"
    TONGA = "on"
    TSONGA = "ts"
    TSWANA = "tn"
    TURKISH = "tr"
    TURKMEN = "tk"
    TWI = "tw"
    UIGHUR = "yg"
    UKRAINIAN = "uk"
    URDU = "ur"
    UZBEK = "uz"
    VENDA = "ve"
    VIETNAMESE = "vi"
    VOLAPüK = "vo"
    WALLOON = "wa"
    WELSH = "cy"
    WOLOF = "wo"
    XHOSA = "xh"
    YIDDISH = "yi"
    YORUBA = "yo"
    ZHUANG = "hu"
    ZULU = "zu"
