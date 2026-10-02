def search_product_knowledge(query: str) -> dict:
    return {
        "query": query,
        "documents": [{
            "title": "Monitor compatibility guide",
            "source": "compatibility_manual.pdf",
            "excerpt": "HDMI 2.1 supports 4K at 120Hz; USB-C to DisplayPort is supported.",
            "citation": "compatibility_manual.pdf#display",
        }],
        "retrieval_count": 1,
    }
