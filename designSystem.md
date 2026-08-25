# 202 · Design System

> Documento **destilado** dos materiais existentes — não é uma identidade nova.
> Cada regra traz sua origem entre parênteses para auditoria. Onde as fontes
> não definem ou divergem, o item vai para **Decisões pendentes** no fim.
>
> **Papel deste arquivo:** governança. Registra as regras *e* como foram
> derivadas (proveniência) *e* o que ainda é incerto (pendências). Serve para
> auditar, decidir pendências e reprocessar sem regredir decisões. **Não é** o
> arquivo carregado a cada criativo — para isso existe o operacional enxuto
> `design.rules.md`, derivado deste.
>
> **Status de ciclo:** o projeto roda em dois ciclos. **Ciclo 1 = Instagram
> (ativo).** **Ciclo 2 = LinkedIn (em espera, com publicações reais da 202 já
> identificadas como insumo).** Quase todo este documento é **transversal** e
> fica **congelado** a partir do Ciclo 1; o Ciclo 2 só *adiciona* seções
> específicas de plataforma, sem reabrir a fundação comum.

## Nota sobre as fontes usadas

| Fonte | Peso | Status nesta destilação |
|---|---|---|
| Pitch deck (`202Pitch.pdf`) | Canônico | Usado |
| `betaDesign.md` (design.md existente) | Canônico | Usado |
| Site da 202 (`202Lab-site.html`) | Canônico | **Recebido** (página Next.js salva). CSS externo (`_files/*.css`) não veio junto e o corpo é hidratado via JS, então só o `<head>`, o hero estático e os atributos de marcação puderam ser lidos — mas isso já confirma fontes, fundo e vários elementos. |
| Post da 202 no Instagram (`insta1–6`) | Amostra real de feed | Usado como amostra única |
| Instagram da parceira "the founders" (`insta_parceiro1–7`) | Referência externa (só mecânica) | Usado apenas para diagramação; **nada de cor/tipo/marca importado** |

**O que o site permitiu confirmar** (re-auditoria da versão anterior deste doc):
famílias tipográficas, fundo `#0a0a0a`, wordmark `202Lab.`, e um hero animado
antes só descrito no design.md. Itens que eram "a confirmar" por dependerem só do
pitch foram promovidos a **regra forte** onde o site concordou (marcados abaixo).
Limite: as regras de cor/escala detalhadas moram no CSS externo não recebido — o
que veio do site é o `<head>` (fontes, preloads, fundo) e o HTML do hero.

---

## 1. Paleta de cores

Tokens vêm do `betaDesign.md` (canônico). A proporção de uso — ~90% preto/branco,
~8% cinzas, ~2% verde — é regra forte, reforçada pela amostra de feed (o verde
aparece só no ponto final, num sublinhado e em uma ou outra palavra).

| Token | Hex | Nome | Uso | Origem |
|---|---|---|---|---|
| `--preto-202` | `#0A0A0A` | Preto 202 | Fundo padrão dark (nunca `#000` chapado em áreas grandes) | **canônico — design.md + site** (`#0a0a0a` é o único hex inline do site) |
| `--preto-puro` | `#000000` | Preto puro | Sobreposições, vinhetas, impressos | canônico — design.md |
| `--branco-202` | `#FFFFFF` | Branco 202 | Texto sobre preto; fundo light | canônico — design.md + feed |
| `--papel` | `#F4F2ED` | Papel | Fundo light alternativo (editorial, decks claros) | canônico — design.md; usado no post "exame"/"construtores" do feed |
| `--cinza-texto` | `#8B8B85` | Cinza texto | Microcopy mono, metadados, legendas, subtítulos de apoio | canônico — design.md + feed (subtítulos cinza) |
| `--cinza-linha` | `#262626` | Cinza linha | Hairlines, bordas, grids sobre preto | canônico — design.md |
| `--cinza-linha-light` | `#D9D6CE` | Cinza linha (light) | Hairlines sobre papel | canônico — design.md |
| `--verde-sinal` | `#C6FF3E` | Verde Sinal | **Verde oficial da marca.** Acento sobre preto: ponto final, links ativos, dados vivos, sublinhado de destaque | **regra forte — design.md + site + feed** (confirmado no CSS: `--verde-sinal:#c6ff3e`) |
| `--verde-tinta` | `#3D7A00` | Verde tinta | Verde para fundos claros (o Sinal falha contraste sobre branco) | canônico — design.md; consistente com o ponto verde escuro no post "construtores." sobre papel |
| `--fio-estrutura` | `#33332E` | Fio estrutura | Hairlines/malha construtiva do site (linhas de construção sobre preto) | **canônico — CSS do site** (`--fio-estrutura:#33332e`) |
| `--verde-codigo` | `#28D305` | Verde código | **Efeito do hero apenas** (digitação/"código" da malha animada). **NÃO é cor de marca** — não usar em criativos | **canônico — CSS do site** (`--verde-codigo:#28d305`); escopo restrito ao hero por decisão |
| `--padrao-repouso` | `#171717` / `#101010` | Padrão repouso | Cinza de fundo da malha em repouso (web) | canônico — CSS do site (`--padrao-repouso`; dois valores entre os módulos) |

**Regras de cor (canônico — design.md; CSS confirma tokens):**
- **Verde oficial da marca = `--verde-sinal #C6FF3E`.** O `--verde-codigo #28D305` é efeito do hero, não cor de marca; nunca entra em criativo.
- Verde nunca em área grande, nunca como fundo de seção, nunca em texto longo. Quanto menos verde, mais forte ele fica.
- Sobre fundo claro, `--verde-sinal` só em elementos ≥ bold ou ≥ 24px; texto verde em fundo claro usa `--verde-tinta`.
- `--fio-estrutura`, `--verde-codigo` e `--padrao-repouso` são **tokens de contexto web** (hero/malha), não da paleta de criativos. Registrados aqui para completude do sistema.
- Não existem outras cores de marca além das acima.
- Cores por frente (Build/Growth/AI) são tese futura — **não externalizar** antes de alinhar coerência (ver Decisões pendentes).

---

## 2. Tipografia

Quatro vozes com papéis fixos (decisão do fundador, 07/07/2026 — canônico, design.md).
**O site confirma a tríade Fraunces + IBM Plex Mono + Inter** — as três aparecem
declaradas na classe raiz do `<html>` e nos preloads de fonte, o que promove o stack
a **regra forte** (pitch + site + design.md).

| Voz | Fonte | Papel | Origem |
|---|---|---|---|
| Marca | The Seasons | **Só** logo/wordmark (`202Lab.`, `202`), que é SVG/imagem. Nunca em texto corrente. | canônico — design.md; wordmark visível no feed e no hero do site |
| Display | Fraunces (`opsz 144`, Google Fonts) | Títulos, frases-mãe, números gigantes | **regra forte — design.md + site + feed** (classe `fraunces_…variable` na raiz do site) |
| Técnica | IBM Plex Mono (Google Fonts) | Labels UPPERCASE (tracking +8–12%), coordenadas, metadados, nav, botões-texto, código | **regra forte — design.md + site + feed** (classe `ibm_plex_mono_…variable`; nav "A TESE", "CONTATO ↗", toggle PT/EN) |
| Corpo/UI | Inter (Google Fonts) | Parágrafos, interface da plataforma, tudo que só precisa funcionar | **regra forte — design.md + site + feed** (classe `inter_…variable`) |

**Por que The Seasons não é usada em texto:** os arquivos disponíveis são
Fontspring DEMO (licença de mockup, proibido em produção; charset de 95 glifos,
sem acentos — todo "ó/ã/ç" cai no fallback). Ela vive só no logo em SVG. Comprar
a licença completa é opcional e só para eventual texto corrente. (canônico — design.md)

### Regras de composição (canônico — design.md)
- **Título tratamento "B"** (escolhido pelo fundador): serifa reta + parte complementar em Light 300, cor `#d5d5d0`, + ponto verde final. Contraste de **peso**, não de estilo. No conteúdo, o frontmatter separa `titulo` (parte forte) e `complemento` (parte leve, opcional). Ex.: "Do problema real ao primeiro protótipo(light)."
- **Itálico:** nunca o swashy em trechos longos. Ênfase = itálico da Fraunces em no máximo uma palavra/trecho curto. *(Reforçado pela amostra de feed: "builders AI-native", "celeiro", "precisa", "futuro", "construtores", "ITA" todos em itálico curto.)*
- **Mono:** nunca em frase longa; sempre curto, uppercase, cinza (`--cinza-texto`) ou verde quando for dado "vivo".
- **Corpo:** Inter 16–18px, entrelinha 1.6, largura máx. ~65ch.

### Escala (canônico — design.md)
| Nível | Tamanho | Origem |
|---|---|---|
| Título de prática/conteúdo | `clamp(2.6rem, 5.5vw, 4rem)` | canônico — design.md |
| Hero | `clamp(3rem, 10vw, 9rem)` | canônico — design.md |
| Corpo | 16–18px / 1.6 | canônico — design.md |
| Mono label | 11–12px, uppercase, tracking 0.1em | canônico — design.md |

- **Evitar tamanhos médios burocráticos:** a marca fala grande ou fala pequeno. (canônico — design.md)

---

## 3. Regras de layout

- **Título display + ponto verde final** como unidade de fechamento de headline. (canônico — design.md + feed, presente em quase todos os cards)
- **Kicker mono uppercase** ancorando o topo da composição, acima do título display, em `--cinza-texto`. (design.md descreve mono-labels + feed; o site usa mono uppercase na nav "A TESE"/"CONTATO ↗" e no toggle "PT / EN" — mecânica confirmada, diagramação de kicker sobre título ainda **a confirmar** no corpo do site)
- **Nav do site:** links mono uppercase no topo — `A TESE`, `CONTATO ↗` — mais toggle de idioma `PT / EN`. Seta `↗` como marcador de link externo/ação. (canônico — site)
- **Subtítulo de apoio** em Inter/`--cinza-texto` abaixo do título, curto (1–2 linhas). (amostra de feed; consistente com regra de corpo do design.md)
- **Wordmark `202Lab.`** no hero (site) e no rodapé do card (feed), discreto. (canônico — site + feed)
- **Muito respiro / preto profundo:** composição editorial com título ocupando faixa vertical central e vazio deliberado em volta. (canônico — design.md "elegância, muito respiro" + feed)
- **Números gigantes / "202" como marca d'água** de baixo contraste atrás do texto. (amostra de feed — card "Potencializamos talentos"; alinhado ao "números gigantes" do design.md)

### Grid e medidas — WEB (confirmado pelo CSS do site)
- **Margem base:** `--margem: 3rem` (desktop), `1.5rem` (mobile ≤720px). (CSS: `:root` + media query)
- **Estrutura da tela:** `.tela` é grid de três faixas verticais — `grid-template-rows: auto 1fr auto` = **topo / centro / base**, altura `100dvh`, padding = `--margem`. (CSS)
- **Label mono:** `--text-label: .75rem`, `--tracking-label: .1em`, uppercase, `--cinza-texto`, `line-height 1.7`. (CSS — confirma a regra de mono-label)
- **Oneliner (display do site):** `clamp(1.5rem, 2.6vw, 2.4rem)`, Fraunces `opsz 144`, weight 300, `letter-spacing -.01em`, `line-height 1.18`. (CSS)
- ⚠️ **Estas medidas são do SITE, não do card de Instagram.** O grid de três faixas e a margem `3rem` valem para web. O card 4:5 tem métrica própria — **medida na amostra real, ver abaixo**.

### Métrica do card de Instagram (MEDIDA na amostra real — Ciclo 1)
Levantada por análise de pixel dos 6 cards do carrossel (`insta1–6`, todos 1296×1620).

| Medida | Valor | Como foi obtido |
|---|---|---|
| Canvas | **1296 × 1620 px** (4:5 exato) | dimensão dos 6 cards |
| Margem lateral | **~124 px** (≈9.6% da largura) | 1ª coluna de texto claro: 119–126px nos 4 cards de texto; wordmark inicia em 124–126px |
| Margem superior | **~128 px** | kicker mono começa em y≈132 (C3, C5) |
| Margem inferior | **~128 px** | baseline do wordmark a 125–145px do fundo |
| Kicker (topo) | mono uppercase, `--cinza-texto`, baseline ~132px do topo, na margem esquerda | C3 "O NOVO PANORAMA", C5 "Como resolvemos?" |
| Wordmark (base) | rodapé esquerdo, alinhado à margem lateral, baseline ~124px do fundo | C1, C5 |
| "arraste →" (base) | rodapé direito, mono `--cinza-texto`, alinhado à margem direita (~124px) | C1 |
| **Faixa de imagem** (meia-composição) | **39% superior** da altura (~632px); texto nos 61% inferiores; imagem sempre ACIMA, corte reto | C2 (ITA) corta em y≈633 (0.390); C4 (exame) em y≈629 (0.388) — **convergência dos dois cards de imagem** |

**Sistema implícito:** margem uniforme de ~124px (≈9.6% da largura) em todos os lados; grade
vertical de três faixas (topo=kicker / centro=título+subtítulo / base=wordmark+navegação),
espelhando o grid `.tela` do site (`auto 1fr auto`). A margem escala como **~9.6% da largura**
se o canvas mudar. A linha de corte da meia-composição é **regra forte** (dois cards independentes
convergem em ~39%).

---

## 4. Uso de logo e marca

- **Wordmark:** `202Lab.` — "202 Lab" em The Seasons + **ponto verde** final. Variante curta `202`. É SVG/imagem, sem dependência de licença web. (canônico — design.md + feed + site: `aria-label="202Lab"`, `<title>202Lab — …`, `data-logo`)
- **Bilíngue:** o site oficial roda em **PT-BR e EN** (toggle `PT / EN`, `<html lang="pt-BR">`). A marca precisa funcionar nos dois idiomas — considerar ao definir copy e frases-mãe. (canônico — site)
- **O "202" tem leitura conceitual:** metade de 404 ("onde muitos veem 'não encontrado', a 202 vê espaço para criação"); origem no quarto 202 do ITA em São José dos Campos, cujas coordenadas entram como metadado de marca. (canônico — design.md + pitch reforça o vínculo com o ITA)
- **Nomenclatura (RESOLVIDO — decisão do fundador):** grafia é **contextual**, não única.
  - **Logo / escrita grande / título:** `202Lab.` (The Seasons + ponto verde). Grafia oficial da marca.
  - **Rodapé / assinatura de deck e PDF:** `202LAB` (caixa alta, sem ponto), como no pitch. Aqui o `202LAB` **não é desalinhamento** — é o uso de rodapé institucional.
  - **Rodapé do card de Instagram:** `202Lab.` com ponto verde (segue a amostra de feed, não o deck).
  Ou seja: `202Lab.` em logo/título e em rodapé de Instagram; `202LAB` só em rodapé/assinatura de deck/PDF.
- **Ponto verde:** menor elemento da marca e o mais importante depois do "202". Sempre círculo perfeito, sempre Verde Sinal. Encerra frases-chave, marca item ativo, pisca como cursor, aponta o "agora". (canônico — design.md + feed)
- Área de proteção / clear space, tamanho mínimo, versões mono do logo: **não definidos** → Decisões pendentes.

---

## 5. Elementos gráficos recorrentes

| Elemento | Descrição | Origem |
|---|---|---|
| **Ponto verde (.)** | Assinatura universal: fim de headline, bullet ativo, status, cursor. Círculo perfeito, Verde Sinal. | canônico — design.md + feed |
| **Dot-matrix** | Tipografia/formas gigantes rasterizadas em malha de `+` ou `·`. Uso: heros, aberturas, capas. Cinza ~`#2E2E2E` sobre preto. | canônico — design.md; feed usa um campo de "202" repetido no fundo (parente do dot-matrix) |
| **Linhas construtivas** | Hairlines de 1px que "constroem" o glifo/composição: eixos que atravessam a tela, círculos de construção, ponto verde na interseção. "Consultoria que constrói." | canônico — design.md; feed card "skin in the game" usa hairline separando título de subtítulo |
| **Mono-labels** | Pares de metadado técnico nos cantos: coordenadas, timestamp, versão, status. `IBM Plex Mono 11–12px, uppercase, tracking 0.1em, --cinza-texto`. | canônico — design.md |
| **Hairline + label** | Linha horizontal fina conectando um label mono a um conteúdo. | canônico — design.md + feed |
| **Sublinhado verde** | Destaque de palavra/linha com traço `--verde-sinal` sob texto display. | **regra forte — confirmado como padrão de marca** (decisão do fundador) |
| **Marca d'água "202"** | Numeral gigante de contorno/baixo contraste atrás do texto. | **regra forte — confirmado como padrão de marca** (decisão do fundador) |
| **Tratamento de imagem (CONDICIONAL)** | **Só quando o card exibe imagem/print externo** (recorte de imprensa, foto): foto em **preto e branco / dessaturada**, em **meia-composição — imagem sempre ACIMA, na proporção da amostra**, texto sobre preto embaixo. **Cards de puro texto NÃO usam foto** (tipografia sobre fundo preto ou papel). | **regra forte — decisão do fundador** (refina a amostra: cards ITA/"exame" eram os que traziam imagem externa) |
| **Hero animado (web)** | Abertura do site anima o wordmark/frase-mãe letra a letra sobre um campo de glifos, com efeito **"lanterna"** (spotlight que revela), **cursor piscante**, **pulso** e **vinheta**. Marcação: `data-glifo/-glifos`, `data-lanterna` (+ `--lanterna-x/-y`, `--escala-lanterna`), `data-ponto`, `data-cursor`, `data-vinheta`, `data-fase/-abertura`. | **canônico — site** (novo; concretiza o "cursor que pisca / ponto que aponta o agora" do design.md) |

### Tensão conceitual que É a marca (canônico — design.md)
"McKinsey menos enterprise, mais mão na massa." Toda peça sobrepõe dois mundos:

| Editorial (consultoria de elite) | Técnico (quem constrói) |
|---|---|
| Serifa de alto contraste (The Seasons/Fraunces) | Monospace uppercase, tracking largo |
| Itálico como ênfase, ritmo de revista | Coordenadas, labels, hairlines, crop marks |
| Preto profundo, muito respiro | Dot-matrix, grids construtivos |
| Elegância, autoridade, permanência | Verde ácido: pulso, sinal vivo, execução |

**Regra de ouro:** nenhuma peça usa só um dos mundos. Serifa sem elemento técnico
vira banca de advocacia; técnico sem serifa vira "mais uma startup". A sobreposição
é a 202.

### Tokens de movimento (web) — canônico, site
Extraídos do hero do site. Registrados como observados; o CSS externo que os consome
não veio, então tratam-se de **valores reais mas de escopo a confirmar** (podem ser
específicos do hero, não globais).

| Token | Valor | Papel provável |
|---|---|---|
| `--d-caractere` | 34ms | Intervalo entre caracteres na digitação |
| `--d-apagar` | 14ms | Velocidade de "apagar" texto |
| `--d-cursor` | 240ms | Ciclo do cursor piscante |
| `--d-pulso` | 360ms | Duração do pulso |
| `--d-topo` | 520ms | Entrada do topo/nav |
| `--d-crescimento` | 1200ms | Crescimento/escala (lanterna?) |
| `--t-troca` | 120ms | Troca de estado |
| `--t-pulso` | 1200ms | Timing do pulso |
| `--t-topo` | 1710ms | Timing do topo |
| `--t-frase` | 2310ms | Duração total da frase animada |

Assinatura de movimento coerente com a marca: **digitação técnica + cursor + pulso
verde** = "sinal vivo, execução, o agora". Reforça o ponto verde como pulso.

---

## 6. Do's e Don'ts

**Do (característico da 202):**
- Título display serifado de alto contraste + ponto verde final. (canônico + feed)
- Verde como acento raro e cirúrgico (~2%). (canônico + feed)
- Mono uppercase curto para kickers/metadados. (canônico + feed)
- Preto `#0A0A0A` (não `#000`) em áreas grandes; muito respiro. (canônico)
- Sobrepor sempre o mundo editorial e o técnico na mesma peça. (canônico)
- Ênfase por itálico da Fraunces em 1 palavra. (canônico + feed)

**Don't (quebra a identidade):**
- Verde em área grande, como fundo de seção ou em texto longo. (canônico)
- The Seasons em texto corrente (licença DEMO + charset sem acento). (canônico)
- Itálico swashy em trechos longos. (canônico)
- Mono em frases longas. (canônico)
- Tamanhos tipográficos médios "burocráticos". (canônico)
- `#000` chapado em grandes áreas. (canônico)
- Importar cor/tipo/marca de referências externas (ex.: azul, asterisco e grafia da parceira "the founders") — isso é **referência de mecânica de post apenas**. (regra desta destilação)

---

## 7. Especificidades por plataforma

> **Recorte de ciclo:** **Instagram é a superfície ativa (Ciclo 1).** A coluna
> "Institucional (pitch)" e "Site" entram como contexto de marca. **LinkedIn ainda
> não tem coluna aqui** — não por esquecimento, mas porque não há amostra de design
> de LinkedIn nos materiais. A coluna de LinkedIn será **adicionada no Ciclo 2**,
> quando as publicações reais da 202 forem processadas. Nada abaixo muda; só se
> acrescenta.

Diferenças **observáveis** entre as três superfícies:

| Aspecto | Institucional (pitch — canônico) | Site (canônico) | Instagram (amostra de feed) — **Ciclo 1 ativo** |
|---|---|---|---|
| Proporção | Deck landscape/slide | Página web responsiva | Card retrato (~4:5), carrossel com "arraste →" e wordmark no rodapé |
| Densidade | Mais texto, dados, timeline | Hero minimalista + movimento; corpo hidratado via JS | Um pensamento por card, muito respiro |
| Fundo | Preto e faixas de cor sólida | Preto `#0a0a0a` | Alterna preto `#0A0A0A` e papel `#F4F2ED`; foto P&B em meia-composição |
| Wordmark | "202 LAB" caixa alta | "202Lab." (`data-logo`, aria-label) | "202Lab." com ponto verde no rodapé esquerdo |
| Movimento | Estático | **Hero animado** (lanterna, cursor, pulso, digitação) | Estático (carrossel) |
| Idioma | PT | **PT + EN** (toggle) | PT |
| Nav | — | Mono uppercase: A TESE · CONTATO ↗ · PT/EN | Kicker mono + "SWIPE/arraste" |

> Tudo na coluna Instagram vem de **uma única amostra**. São observações, não regras
> de plataforma — não elevar idiossincrasias do post a padrão sem uma segunda peça.
> O layout de carrossel (kicker no topo, "SWIPE"/"arraste", numeração "n/6") é
> **mecânica de post** e coincide com a referência externa da parceira; adote a mecânica,
> **não** a estética dela (nada de azul, asterisco, grifo azul ou grafia "the founders").

---

## Decisões pendentes

> Reclassificadas por ciclo. **[JÁ]** = decidir agora, bloqueia o Ciclo 1.
> **[BUSCAR]** = material a recuperar antes do piloto do Ciclo 1 (ganho grande, não bloqueio).
> **[C2]** = pertence ao Ciclo 2 (LinkedIn). **[FUTURO]** = tese futura / cosmético, não trava nada.

1. ~~**Grafia oficial do wordmark**~~ — **RESOLVIDO.** Contextual: `202Lab.` em logo/título e rodapé de Instagram; `202LAB` em rodapé/assinatura de deck/PDF. (ver §4)
2. ~~**Grid, margens e colunas (web)**~~ — **RESOLVIDO para web.** CSS confirma `--margem: 3rem`/`1.5rem` e grid `.tela` de três faixas (`auto 1fr auto`). (ver §3) — *Falta ainda a métrica do card 4:5 de Instagram, a definir no piloto.*
3. ~~**CSS externo do site**~~ — **RESOLVIDO.** CSS recebido; cores, tokens de fonte, margem e movimento confirmados e incorporados (§1, §2, §3, §5).
4. **[FUTURO] Cores por frente (Build / Growth / AI):** "tese futura, não externalizar" (design.md). Decidir se entram e como convivem com "não existem outras cores".
5. **[FUTURO] Logo — área de proteção, tamanho mínimo, versões mono/reversa:** não definidos em nenhuma fonte.
6. ~~**Tratamento de imagem**~~ — **RESOLVIDO.** Condicional: P&B + meia-composição (imagem sempre acima, proporção da amostra) só quando há imagem/print externo; cards de texto não usam foto. (ver §5)
7. ~~**Sublinhado verde e marca d'água "202"**~~ — **RESOLVIDO.** Ambos confirmados como padrão de marca. (ver §5)
8. ~~**Métrica do card 4:5 de Instagram**~~ — **RESOLVIDO.** Medida na amostra real (6 cards): canvas 1296×1620, margem ~124px (≈9.6%) uniforme, grade de 3 faixas, faixa de imagem 39% no topo. (ver §3)
9. **[FUTURO] `--verde-tinta` em fundo claro:** conferir o hex do ponto verde do post "construtores." (sobre papel) contra o token.
10. **[FUTURO] Bold Italic:** The Seasons não tem; definir como resolver ênfase bold+itálico no display (via Fraunces).
11. **[FUTURO] Tokens de movimento (web):** valores reais confirmados no CSS (`--d-caractere 34ms`, `--d-cursor 240ms`, `--corrida 2.8s`, `--largada .5s`, etc.). Definir se viram escala global de motion. (Web; não afeta Instagram estático.)
12. **[C2/FUTURO] Versão EN da marca:** o site é bilíngue. Definir tratamento das frases-mãe e da copy em inglês.
13. **[FUTURO] Sistema de navegação:** `A TESE` e `CONTATO ↗` são os únicos itens vistos. Confirmar arquitetura de nav completa e o padrão da seta `↗`. (Web.)
