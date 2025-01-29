import React, { useState } from "react";
import "./Home.css";

function Home() {
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [selectedSubCategory, setSelectedSubCategory] = useState(null);

  const categories = [
    { name: "Electronics", subCategories: ["Phones", "Laptops", "Cameras"] },
    { name: "Clothing", subCategories: ["Men", "Women", "Kids"] },
    { name: "Home Appliances", subCategories: ["Refrigerators", "Washers", "Microwaves"] },
  ];

  const products = [
    { name: "iPhone 13", category: "Phones" },
    { name: "MacBook Pro", category: "Laptops" },
    { name: "Nikon D750", category: "Cameras" },
    { name: "Men's Jacket", category: "Men" },
    { name: "Refrigerator LG", category: "Refrigerators" },
  ];

  const filteredProducts = products.filter(
    (product) =>
      (!selectedCategory || product.category === selectedCategory) &&
      (!selectedSubCategory || product.category === selectedSubCategory)
  );

  return (
    <div className="home-container">
      {/* Header */}
      <header className="header">
        <div className="brand">
          <img src="/logo.png" alt="Brand Logo" className="logo" />
          <span className="brand-name">MyShop</span>
        </div>
        <nav className="nav-links">
          <a href="#home">Home</a>
          <a href="#categories">Categories</a>
          <a href="#contact">Contact</a>
        </nav>
        <div className="search">
          <input type="text" placeholder="Search products..." />
          <button className="search-button">🔍</button>
        </div>
      </header>

      {/* Main Section */}
      <main className="main">
        <aside className="sidecar">
          <ul className="categories">
            {categories.map((category) => (
              <li
                key={category.name}
                className={selectedCategory === category.name ? "active" : ""}
                onClick={() => setSelectedCategory(category.name)}
              >
                {category.name}
                {selectedCategory === category.name && (
                  <ul className="subcategories">
                    {category.subCategories.map((subCategory) => (
                      <li
                        key={subCategory}
                        className={selectedSubCategory === subCategory ? "active" : ""}
                        onClick={() => setSelectedSubCategory(subCategory)}
                      >
                        {subCategory}
                      </li>
                    ))}
                  </ul>
                )}
              </li>
            ))}
          </ul>
        </aside>
        <section className="product-display">
          {filteredProducts.length > 0 ? (
            <div className="product-list">
              {filteredProducts.map((product) => (
                <div key={product.name} className="product-card">
                  <h3>{product.name}</h3>
                </div>
              ))}
            </div>
          ) : (
            <p className="no-products">No products found.</p>
          )}
        </section>
      </main>
    </div>
  );
}

export default Home;