# Make the Judge Laugh in One Line — Entry Preview

- **Bounty:** `u-email-baru-make-the-judge-laugh-in-one-line-791ccb21`
- **Title:** Make the Judge Laugh in One Line
- **Category:** Growth · Reward $2 (juara 1 & 2 masing-masing $1) · Entry gratis
- **Deadline:** 2026-11-26T22:30:00Z (= 27 Nov 2026 05:30 WIB)
- **Status:** DIBANGUN, **BERHENTI DI PREVIEW — BELUM SUBMIT** (submit hanya atas lampu hijau eksplisit user)

## Aturan yang dipakai (dari RULES.txt + competition.yaml)

- Program entry (program/v1) menulis SATU teks ke `/output/entry.txt`.
- Gate: teks UTF-8, 1–200 karakter, bukan hanya spasi kosong.
- Juri (z-ai/glm-5.3-flash) membandingkan dua baris sekaligus, kriteria berurutan:
  1. Lucu dalam sekali baca, dipahami orang asing tanpa konteks.
  2. Surprise: membangun ekspektasi lalu mematahkannya.
  3. Tight: tiap kata berguna, punchline di akhir, tidak dijelaskan.
  4. Fresh: bukan joke pasaran, bukan pun yang sudah sering didengar.
  5. Terbaca bersih saat diucapkan, tanpa referensi yang butuh konteks.
- Repo GitHub **WAJIB** (program/v1, transcripts_required: true, repo dibuat setelah
  kompetisi buka 2026-11-26T03:31:44Z, LICENSE OSI, README berisi 3 badge make.fun,
  GitHub About berisi website make.fun + topic `makefun`).
- Repo: `mihawnk-nft/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21` (public).

## Kandidat (semua dalam bahasa Inggris, ≤200 karakter)

| # | Baris | Karakter | Byte |
|---|-------|----------|------|
| A | My grandfather warned me never to trust a man with two first names. His name was James James. | 93 | 93 |
| B | I asked my GPS for the meaning of life. It said, 'Recalculating' — which explains my twenties. | 94 | 96 |
| C | I tried to sue the airline for losing my luggage, but I lost the case. | 70 | 70 |
| D | My horoscope said I'd meet a tall, dark stranger today. I met a giraffe, so technically it counts. | 98 | 98 |
| E | I asked my plants for advice. They said nothing — the most growth I've seen from them in months. | 96 | 98 |

### Penilaian per kandidat (kriteria juri, berurutan)

- **A — DIPILIH.** Setup: nasihat kakek yang terdengar bijak. Twist di kata terakhir:
  si kakek sendiri bernama "James James" — dua nama depan — jadi nasihatnya
  mendiskualifikasi dirinya sendiri. Surprise murni di akhir, tiap kata berguna,
  payoff "James James" bukan punchline pasaran, dan langsung dipahami sekali baca.
- **B.** Swerve bagus ("Recalculating" → "explains my twenties"), tapi trope GPS
  "recalculating" sudah familiar — kalah fresh dari A.
- **C.** Paling tight (70 karakter) dan twist "lost the case" rapi, tapi joke ini
  sudah beredar luas sebagai one-liner klasik — risiko kalah di kriteria freshness.
- **D.** Payoff jerapah lucu dan orisinal, tapi setup horoskop agak panjang dan
  punchline-nya lebih "imut" daripada "ngakak" — surprise-nya lebih lemah dari A.
- **E.** Wordplay "growth" rapi, tapi keluarga pun tanaman sudah sering dipakai —
  kalah fresh dari A.

## PILIHAN FINAL

> My grandfather warned me never to trust a man with two first names. His name was James James.

- **Jumlah karakter: 93** (batas 200) · **93 byte** · UTF-8, satu baris, tanpa newline di akhir.
- File entry: `main.py` (pure stdlib) menulis baris ini ke `/output/entry.txt`.

## Validasi lokal

- `python3 main.py` → `/output/entry.txt` berisi tepat baris final di atas (93 karakter,
  valid UTF-8, bukan spasi kosong). Lolos gate 1–200 karakter.
- Kit check (`node cli/makefun.mjs check`): lihat bagian "Kit check" di bawah.

## Kit check

- Repo dibuat + push ke GitHub: YA (lihat repo di atas).
- `check` butuh bundle transkrip (`--transcripts transcripts.tar.gz`); bundle
  transkrip sesi build ini harus dibuat dari sesi top-level (parent agent) setelah
  subagent selesai — jadi check penuh dijalankan saat submit, bukan dari run ini.
- Yang sudah diverifikasi di run ini: gate lokal (panjang/UTF-8), README + 3 badge,
  LICENSE MIT, GitHub About (website + topic `makefun`), repo dibuat setelah buka.

## Yang TIDAK dilakukan di run ini

- TIDAK submit, TIDAK klaim hadiah, TIDAK ubah seen.json, TIDAK hubungi pihak mana pun.
