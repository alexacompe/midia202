# 202 · Regras de design (operacional)

Arquivo carregado pela skill a cada criativo. Só regras acionáveis. Escopo: **Instagram (Ciclo 1)**.
Racional, fontes e pendências ficam em `design-system.md` (governança).

## Valores (tokens)

```
# Cores
--preto-202        #0A0A0A   fundo dark padrão (nunca #000 chapado em área grande)
--preto-puro       #000000   sobreposições, vinhetas
--branco-202       #FFFFFF   texto sobre preto; fundo light
--papel            #F4F2ED   fundo light alternativo (editorial)
--cinza-texto      #8B8B85   microcopy mono, metadados, legendas, subtítulos
--cinza-linha      #262626   hairlines/bordas sobre preto
--cinza-linha-lt   #D9D6CE   hairlines sobre papel
--verde-sinal      #C6FF3E   VERDE OFICIAL DA MARCA. acento sobre preto (ponto final, link ativo, dado vivo)
--verde-tinta      #3D7A00   verde para fundo claro (contraste)
# (verde-codigo #28D305 é efeito do hero do site — NÃO usar em criativos)

# Fontes
marca      The Seasons     só logo/wordmark (SVG). Nunca em texto.
display    Playfair Display  títulos e ênfase itálica dos CARDS (bate com carrossel real)
#          Fraunces          usada no SITE — ver pendência de tipografia no SKILL.md
técnica    IBM Plex Mono   labels UPPERCASE, coordenadas, metadados, nav
corpo/ui   Inter           parágrafos, interface

# Escala
titulo-conteudo  clamp(2.6rem, 5.5vw, 4rem)
hero             clamp(3rem, 10vw, 9rem)
corpo            16–18px / entrelinha 1.6 / máx ~65ch
mono-label       11–12px / uppercase / tracking 0.1em

# Proporção de cor alvo
~90% preto/branco · ~8% cinzas · ~2% verde
```

## Regras de cor
- Verde é acento raro e cirúrgico (~2%): ponto final, link ativo, dado vivo, sublinhado de destaque. Quanto menos verde, mais forte ele fica.
- Verde nunca em área grande, nunca como fundo de seção, nunca em texto longo.
- Sobre fundo claro: `--verde-sinal` só em elemento ≥ bold ou ≥ 24px; texto verde em fundo claro usa `--verde-tinta`.
- Áreas grandes de preto usam `--preto-202`, nunca `#000` chapado.
- Fora dos tokens acima, não existem outras cores. Não usar cores por frente (Build/Growth/AI).

## Regras de tipografia
- The Seasons **só** no logo. Nunca em texto corrente (licença DEMO, sem acentos).
- Ênfase = itálico da Fraunces em **no máximo uma** palavra/trecho curto. Nunca itálico swashy em trecho longo.
- Mono sempre curto, uppercase, cinza (ou verde quando for dado vivo). Nunca mono em frase longa.
- Corpo em Inter, 16–18px, entrelinha 1.6, largura máx. ~65ch.
- A marca fala grande ou fala pequeno: evitar tamanhos médios burocráticos.
- Título tratamento "B": parte forte + complemento em peso leve (Light 300, `#d5d5d0`) + ponto verde final. Contraste de **peso**, não de estilo.

## Layout (card de Instagram) — MÉTRICA MEDIDA na amostra real

```
# Canvas
1296 × 1620 px  (4:5 exato)  — fundo --preto-202 ou --papel

# Margem de segurança (medida: texto/wordmark nunca cruza)
lateral (esq/dir)   ~124 px   (≈9.6% da largura)
superior            ~128 px   (≈8% da altura)
inferior            ~128 px   (≈8% da altura)
# Regra escalável: margem = ~9.6% da largura do canvas (para outros tamanhos)

# Grade vertical (3 faixas, como o grid .tela do site: topo / centro / base)
topo    kicker mono uppercase, baseline ~132 px do topo, na margem esquerda
centro  título display (+ subtítulo opcional logo abaixo), ocupa a faixa central
base    wordmark no rodapé esquerdo; "arraste →" no rodapé direito, ambos na baseline ~124-128 px do fundo

# Meia-composição (SÓ card com imagem/print externo)
faixa de imagem = 39% superior da altura (~632 px)  |  texto nos 61% inferiores
imagem sempre ACIMA, corte reto horizontal
```

- Uma ideia por card. Muito respiro, preto profundo, título display na faixa vertical central.
- Kicker mono uppercase (`--cinza-texto`) ancorando o topo, na margem esquerda, ~132px do topo.
- Título display + **ponto verde final** como unidade de fechamento da headline.
- Subtítulo de apoio opcional em Inter/`--cinza-texto`, 1–2 linhas, logo abaixo do título.
- Wordmark `202Lab.` no rodapé esquerdo, alinhado à margem lateral (~124px), baseline ~124px do fundo.
- "arraste →" (mono, `--cinza-texto`) no rodapé direito, alinhado à margem direita. Só em cards que não sejam o último.
- Marca d'água "202" gigante, baixo contraste (contorno `--cinza-linha`), atrás do texto — cards de abertura/fecho.
- Todo texto e todo elemento de rodapé respeitam a margem de ~124px. Nada encosta na borda.

## Logo e marca
- Grafia no card de Instagram: **`202Lab.`** (com ponto verde), no rodapé. Variante curta `202`. (A grafia `202LAB` caixa-alta é só para rodapé de deck/PDF — não usar em Instagram.)
- Ponto verde: sempre círculo perfeito, sempre `--verde-sinal` `#C6FF3E`. Encerra frases-chave, marca item ativo, aponta o "agora".

## Elementos gráficos
- Ponto verde: assinatura universal (fim de headline, bullet ativo, status).
- Dot-matrix / campo de "202" repetido: fundo de heros e capas, cinza sobre preto.
- Linhas construtivas (hairline 1px) e mono-labels de metadado nos cantos (coordenadas, versão, status).
- Tratamento de imagem (**condicional**): *só* quando o card exibe imagem/print externo (recorte, foto) → foto **P&B/dessaturada**, meia-composição com a **imagem sempre acima** (proporção da amostra) e texto sobre preto embaixo. Card de puro texto → **sem foto**, tipografia sobre fundo (preto ou papel).

## Regra de ouro (inquebrável)
Toda peça sobrepõe **editorial** (serifa de alto contraste, itálico-ênfase, respiro) **e técnico** (mono uppercase, coordenadas, hairlines, verde de sinal). Nunca só um dos dois: serifa sozinha vira banca de advocacia; técnico sozinho vira "mais uma startup".

## Nunca (quebra a identidade)
- Verde em área grande, como fundo ou em texto longo.
- The Seasons em texto corrente.
- Itálico swashy longo; mono em frase longa; tamanhos médios burocráticos; `#000` chapado grande.
- Importar cor/tipo/marca/estética de referência externa (parceira "the founders": azul, asterisco, grafia própria). Referência externa é só mecânica de carrossel.
