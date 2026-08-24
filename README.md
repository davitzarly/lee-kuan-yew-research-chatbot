# Weekly IG Post Generator

An AI-assisted workflow concept for generating weekly Instagram content for Rumah123 from property news or topics.

## Objective
Generate consistent, engaging Instagram captions for Rumah123 while maintaining a professional, trustworthy, friendly, and relatable brand voice.

## Workflow
1. Receive a property news/topic as input.
2. Extract the main topic and key facts.
3. Apply the Rumah123 content prompt.
4. Generate an Instagram caption with a hook, practical value, engagement question, and relevant hashtags.
5. Review the output for clarity, factuality, tone, and unsupported claims.

## Example Input
"Tips for first-time homebuyers with a limited budget"

## Example Output
🏡 Mau punya rumah pertama tapi budget masih terbatas?

Tenang, punya rumah bukan cuma soal punya uang banyak. Yang penting adalah punya strategi yang tepat! ✨

💡 3 tips untuk first-time homebuyer:

1️⃣ Tentukan budget realistis dengan menghitung pemasukan, pengeluaran, dan kemampuan cicilan.

2️⃣ Pahami KPR sebelum mengajukan, termasuk DP, bunga, tenor, dan biaya tambahan.

3️⃣ Pilih lokasi dengan bijak dengan mempertimbangkan akses, fasilitas, dan potensi perkembangan area.

💬 Kalau punya budget terbatas, mana yang paling penting: lokasi, luas rumah, atau cicilan ringan?

#Rumah123 #TipsRumah #RumahPertama #KPR #FirstTimeHomeBuyer #PropertiIndonesia #TipsProperti

## AI Usage
The workflow uses a structured prompt to control audience, tone, format, engagement, and safety requirements. The prompt is documented in `prompts.md`.

## Implementation Note
`generator.py` demonstrates the workflow logic using a deterministic template. In production, the `generate_caption()` step can be connected to an LLM API or an automation platform such as n8n/Flowise.
