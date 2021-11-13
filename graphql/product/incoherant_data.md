# Incoherent queries 
## Product
### Products without creator 
query GetProductsWithoutCreator {
  Product(limit: 50, where: {creator: {_is_null: true}}) {
    code
    product_name
  }
}

### Products without url
query GetProductsWithoutURL {
  Product(limit: 50, where: {url: {_is_null: true}}) {
    code
    product_name
  }
}

