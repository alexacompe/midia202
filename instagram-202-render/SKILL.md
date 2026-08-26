---
name: instagram-202-render
description: Renderiza cards de carrossel de Instagram da 202 (202Lab.) a partir de um JSON de conteúdo, produzindo PNGs 1296×1620 fiéis à identidade visual da marca (fontes, cores, métrica e layout medidos da amostra real). Use quando for gerar as IMAGENS de um post de carrossel institucional da 202 para Instagram. NÃO gera o texto/storytelling do post (isso é papel do agente de conteúdo) nem posts de LinkedIn. Requer um renderizador HTML→imagem (Playwright/Chromium preferido; wkhtmltoimage como fallback).
---

# 202 · Render de carrossel de Instagram

Esta skill transforma um **JSON de conteúdo** (um card por objeto) em **PNGs 1296×1620**
prontos para postar, aplicando a identidade visual da 202 (Ciclo 1 — Instagram).

Ela **renderiza**; não decide o conteúdo. O texto, o storytelling e a escolha de imagens
vêm de fora (do agente de conteúdo ou do usuário). A skill garante que o resultado saia
com as fontes, cores, margens e layout corretos da marca.

## Quando usar

- O usuário quer as **imagens** de um carrossel institucional da 202 para Instagram.
- Já existe (ou o usuário fornece) o texto de cada card.

## Quando NÃO usar

- Gerar o texto/tese do post → é papel do agente de conteúdo (voz em `voice.rules.md`).
- Post de LinkedIn → é outro formato (Ciclo 2), com métrica e voz próprias.
- Reels/vídeo → fora de escopo.

## Fundação de referência

Esta skill implementa as regras destiladas em (mantenha-as no repositório, junto):
- `design.rules.md` — regras visuais operacionais (cores, tipografia, métrica do card).
- `voice.rules.md` — regras de voz (consumidas pelo agente de conteúdo, não por esta skill).
Os documentos de governança completos são `design-system.md` e `voice.md`.

## Como usar

1. Monte um JSON descrevendo os cards (ver "Formato do JSON" abaixo).
2. Rode:
   ```
   python3 scripts/render.py <cards.json> --out <pasta_de_saida>
   ```
3. Os PNGs saem como `card1.png`, `card2.png`, … na pasta indicada, em ordem.

O script escolhe o renderizador automaticamente e informa qual usou.

## Formato do JSON

Um objeto com a chave `cards` (lista), ou diretamente uma lista. Cada card aceita:

| Campo | Tipo | Descrição |
|---|---|---|
| `titulo` | string | Título display (Fraunces). Marcação inline: `*itálico*` (ênfase), `_sublinhado verde_`. |
| `ponto` | bool | Ponto verde no fim do título. Padrão `true`. |
| `subtitulo` | string | Texto de apoio (Inter, cinza). Marcação: `**negrito**`, `_sublinhado verde_`. |
| `kicker` | string | Rótulo mono uppercase no topo (ex. "O NOVO PANORAMA"). |
| `escala` | string | Tamanho do título: `"XL"` (curto), `"L"` (padrão), `"M"` (longo). |
| `fundo` | string | `"preto"` (padrão) ou `"papel"` (fundo claro). |
| `ancora` | string | Posição vertical do título: `"center"` (padrão), `"low"` (abertura), `"fecho"`. Ignorado em cards com imagem. |
| `imagem` | string | Caminho de uma **foto limpa** (ver aviso abaixo) para meia-composição. |
| `marca_dagua` | bool | Marca d'água "202" em contorno, atrás do texto (abertura/fecho). |
| `hairline` | bool | Linha fina entre título e subtítulo. |
| `arraste` | bool | Marcador "arraste →" no rodapé direito (cards que não são o último). |

### ⚠️ Aviso importante sobre `imagem`
A skill coloca o texto **por cima/abaixo** da foto. A imagem fornecida deve ser uma
**foto limpa** (só a imagem — prédio, retrato, etc.), **NUNCA um card já com texto**.
Se você passar um card pronto, o texto dele aparecerá junto do texto novo (duplicação).
A faixa de imagem ocupa os **39% superiores** do card; a foto é convertida para P&B
automaticamente. Cards de puro texto não usam `imagem`.

### Exemplo mínimo
```json
{
  "cards": [
    { "titulo": "Conheça uma nova geração de *builders AI-native*", "ancora": "low", "marca_dagua": true, "arraste": true },
    { "kicker": "O NOVO PANORAMA", "titulo": "A 202 é esse _celeiro de mentes brilhantes_",
      "subtitulo": "No novo panorama, destacam-se aqueles que _aprendem rápido_." },
    { "titulo": "Potencializamos talentos e construímos o *futuro*", "escala": "XL", "ancora": "fecho", "marca_dagua": true }
  ]
}
```

## Renderizador (dois motores)

O script (`scripts/render.py`) escolhe automaticamente, nesta ordem:

1. **Playwright + Chromium (PREFERIDO).** Render nativo, fiel, sem perda. Se a lib estiver
   instalada mas faltar o navegador, o script tenta `playwright install chromium` uma vez.
2. **wkhtmltoimage (FALLBACK).** Esse motor *pagina* em canvas alto e duplicaria o texto,
   então o script renderiza em meia escala (648×810) e faz upscale 2× Lanczos. Funciona,
   com leve perda de nitidez ante o Playwright.

Se **nenhum** estiver disponível e não puder ser instalado, o script **para com instrução
clara** — nunca gera um card degradado em silêncio. Para instalar:
- Playwright: `pip install playwright && playwright install chromium`
- wkhtmltoimage: `sudo apt-get install -y wkhtmltopdf`

## Fontes (empacotadas em `assets/fonts/`)

As fontes viajam com a skill (funciona offline, determinístico):
- **Playfair Display** (display, títulos) — instanciada em **peso 500**, roman e itálico. É a
  fonte que **bate com o carrossel real da 202** no Instagram (itálico caligráfico, com swashes).
- **Inter** (corpo/subtítulo) — regular e bold.
- **IBM Plex Mono** (kicker, wordmark, "arraste") — regular.

### ⚠️ Nota de tipografia (pendência aberta)
Há uma **divergência de fonte** entre superfícies da 202, identificada por comparação visual:
- O **site** usa **Fraunces** (confirmado no CSS do site).
- Os **cards de Instagram** usam **Playfair Display** (bate com a amostra real do carrossel).

Esta skill usa **Playfair** para reproduzir fielmente o carrossel existente. Se a 202 decidir
**padronizar em Fraunces** (a fonte da fundação/site), troque o título: as fontes Fraunces já
estão empacotadas (`Fraunces-Display.ttf`, `Fraunces-DisplayItalic.ttf`) — basta apontar o
`@font-face` de `TituloDisplay` para elas em `templates/card.css`. A identificação da Playfair
é por correspondência visual; confirme com o designer da 202 antes de congelar.

The Seasons (fonte do logo) **não** é usada: o wordmark é textual/placeholder aqui; para o
logo oficial em The Seasons, use um SVG (ver "Limitações").

## Limitações conhecidas

- **Wordmark textual.** O rodapé usa "202 Lab." em mono como placeholder. O wordmark oficial
  da 202 é The Seasons (proprietária) e idealmente entra como **SVG**. Se você tiver o SVG do
  logo, substitua o `.wordmark` no template por ele.
- **Escala de título automática.** Escolha `escala` conforme o comprimento do título; títulos
  muito longos podem exigir `"M"`. A skill não quebra linha "inteligentemente" — revise o
  resultado.
- **Fallback com upscale.** Em ambientes sem Chromium, a nitidez é levemente menor. Prefira
  Playwright para qualidade máxima.
- **Métrica calibrada para 1296×1620 (4:5).** Margens e âncoras são medidas desse canvas.

## Estrutura da skill

```
instagram-202-render/
  SKILL.md              (este arquivo)
  scripts/render.py     (motor: JSON → HTML/CSS → PNG)
  templates/card.css    (CSS que codifica a métrica medida da 202)
  assets/fonts/         (Fraunces, Inter, IBM Plex Mono empacotadas)
  references/           (design.rules.md, voice.rules.md — cópias de referência)
```
