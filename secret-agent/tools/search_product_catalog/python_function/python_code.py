def search_product_catalog(query: str = "", category: str = "") -> dict:
  """Searches the Klar Danish furniture product catalog by query or category.

  Args:
    query: Search keywords or product name (e.g. 'dining table', 'lounge chair').
    category: Product category filter (e.g. 'seating', 'tables', 'storage', 'lighting').

  Returns:
    dict: Catalog search results including matching products, materials, and pricing.
  """
  try:
    params = {"query": str(query), "category": str(category)}
    response = ces_requests.get("https://api.klarfurniture.example.com/catalog/search", params=params)
    if response.status_code == 200:
      return {"status": "success", "data": response.json()}
    return {"status": "error", "code": str(response.status_code), "message": response.reason}
  except Exception as e:
    return {"status": "error", "message": str(e)}