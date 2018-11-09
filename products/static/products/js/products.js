const renderProduct = ({ id, title, image }) => (
    `
    <div class="item">
        <a  class="product__link" href="/products/${id}">
            <span class="item-cover-cont">
                <img class="product__cover" src="${image}" alt="${image.title}">
            </span>
            
            <span class="product__name">
                ${ title}
            </span>
        </a>
    </div>
    `
);