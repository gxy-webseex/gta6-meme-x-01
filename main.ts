// gta6-meme-x-01 entry (Node 22, standard library only).
// The entry is the X post itself, not this program: all this program does is
// copy POST.json from the repository root to /output/POST.json, where the
// gate reads the post's address and the house reads the post from X.
// Run it the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const postPath = join(BOT_DIR, 'POST.json');
const post = JSON.parse(readFileSync(postPath, 'utf8'));
if (typeof post !== 'object' || post === null || typeof post.url !== 'string' || post.url.length === 0) {
  throw new Error('POST.json must be a JSON object with a non-empty string "url" field');
}

mkdirSync(OUTPUT_DIR, { recursive: true });
copyFileSync(postPath, join(OUTPUT_DIR, 'POST.json'));
