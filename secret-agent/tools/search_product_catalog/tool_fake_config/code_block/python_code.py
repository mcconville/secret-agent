def fake_tool_call(tool, input_args, callback_context) -> dict:
  v = callback_context.variables or {}
  mc = v.get("mock_context") if isinstance(v.get("mock_context"), dict) else {}
  args = input_args or {}

  catalog = mc.get("catalog") or v.get("catalog")
  if isinstance(catalog, list) and catalog:
    return {"status": "success", "data": {"products": catalog}}
  if isinstance(catalog, dict) and catalog:
    return {"status": "success", "data": catalog}

  q = str(args.get("query", "")).lower()
  cat = str(args.get("category", "")).lower()

  sample_products = [
      {
          "product_id": "KLAR-CHAIR-01",
          "name": "Nordic Oak Lounge Chair",
          "category": "seating",
          "price": 450.00,
          "material": "Solid Oak & Boucle Wool",
          "description": "Minimalist Danish armchair crafted from sustainably sourced solid white oak with soft boucle upholstery.",
          "dimensions": "78cm H x 72cm W x 75cm D",
          "in_stock": True
      },
      {
          "product_id": "KLAR-TABLE-02",
          "name": "Copenhagen Extendable Dining Table",
          "category": "tables",
          "price": 1150.00,
          "material": "Smoked Oak Veneer & Solid Oak Legs",
          "description": "Clean-lined Scandinavian dining table with seamless butterfly extension seating up to 8 guests.",
          "dimensions": "75cm H x 180-240cm W x 90cm D",
          "in_stock": True
      },
      {
          "product_id": "KLAR-STORAGE-03",
          "name": "Aarhus Modular Sideboard",
          "category": "storage",
          "price": 890.00,
          "material": "Oiled Walnut & Matte Brass",
          "description": "Functional Danish modern credenza with slatted tambour doors and adjustable shelving.",
          "dimensions": "70cm H x 160cm W x 45cm D",
          "in_stock": True
      },
      {
          "product_id": "KLAR-LIGHT-04",
          "name": "Fjord Pendant Light",
          "category": "lighting",
          "price": 220.00,
          "material": "Spun Brass & Opal Glass",
          "description": "Warm ambient Scandinavian hanging lamp with frosted diffuser.",
          "dimensions": "35cm Diameter x 28cm H",
          "in_stock": True
      }
  ]

  matches = []
  for p in sample_products:
    if q and (q in p["name"].lower() or q in p["description"].lower() or q in p["category"].lower() or q in p["material"].lower()):
      matches.append(p)
    elif cat and cat in p["category"].lower():
      matches.append(p)

  results = matches if matches else sample_products
  return {"status": "success", "data": {"products": results, "count": len(results)}}