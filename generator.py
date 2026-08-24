from textwrap import dedent

def generate_caption(topic: str) -> str:
    """Generate a Rumah123-style Instagram caption from a topic.

    This demo uses a deterministic template so the workflow can run
    without an external API key. The prompt specification in prompts.md
    can be connected to an LLM in production.
    """
    return dedent(f"""
    🏡 {topic}

    Bingung harus mulai dari mana? Yuk, simak 3 hal penting yang bisa
    membantu kamu mengambil keputusan properti dengan lebih matang! ✨

    💡 3 tips penting:
    1️⃣ Tentukan kebutuhan dan budget secara realistis.
    2️⃣ Bandingkan pilihan berdasarkan lokasi, fasilitas, dan kemampuan cicilan.
    3️⃣ Cek informasi dan biaya tambahan sebelum mengambil keputusan.

    💬 Menurut kamu, apa yang paling penting saat memilih properti: lokasi,
    harga, atau fasilitas?

    #Rumah123 #TipsProperti #PropertiIndonesia #RumahPertama
    #TipsRumah #KPR
    """).strip()


if __name__ == "__main__":
    topic = input("Enter property topic/news: ").strip()
    if not topic:
        topic = "Tips membeli rumah pertama dengan budget terbatas"
    print("\nGenerated Instagram Post:\n")
    print(generate_caption(topic))
