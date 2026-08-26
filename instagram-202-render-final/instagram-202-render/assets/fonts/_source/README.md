# Fontes-fonte (variable) — para reinstanciar

Fontes variable originais (Google Fonts, OFL). As de produção em `../` foram instanciadas
com fonttools.

## Em uso (título dos cards)
- Playfair-Display.ttf       = Playfair @ wght=500   (ATIVA — bate com o carrossel real)
- Playfair-DisplayItalic.ttf = Playfair-Italic @ wght=500 (itálico caligráfico)

## Reserva (caso a 202 padronize o site font nos cards)
- Fraunces-Display.ttf       = Fraunces @ wght=300, opsz=144, SOFT=0, WONK=0
- Fraunces-DisplayItalic.ttf = Fraunces-Italic @ mesmos eixos

## Corpo e mono
- Inter-Reg.ttf / Inter-Bd.ttf = Inter @ wght 400/700
- IBMPlexMono-Regular.ttf      = IBM Plex Mono regular (não-variable)

## Pendência de tipografia
Site = Fraunces (confirmado no CSS). Cards de Instagram = Playfair (correspondência visual
com a amostra real). A skill usa Playfair; para trocar por Fraunces, aponte o @font-face
`TituloDisplay` em templates/card.css para os arquivos Fraunces-Display*. Confirme a fonte
com o designer da 202 antes de congelar.

## Reinstanciar (exemplo)
    from fontTools.varLib.instancer import instantiateVariableFont
    from fontTools.ttLib import TTFont
    f=TTFont('Playfair.ttf')
    instantiateVariableFont(f,{'wght':500},inplace=True)
    f.save('../Playfair-Display.ttf')
