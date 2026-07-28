document.addEventListener("DOMContentLoaded", () => {
  const images = document.querySelectorAll(".ra-lightbox-image");

  if (!images.length) {
    return;
  }

  const overlay = document.createElement("div");
  overlay.className = "ra-lightbox-overlay";
  overlay.innerHTML = `
    <div class="ra-lightbox-content">
      <button class="ra-lightbox-close" type="button" aria-label="Close image">×</button>
      <img class="ra-lightbox-full" src="" alt="">
      <p class="ra-lightbox-caption"></p>
    </div>
  `;

  document.body.appendChild(overlay);

  const fullImage = overlay.querySelector(".ra-lightbox-full");
  const caption = overlay.querySelector(".ra-lightbox-caption");
  const closeButton = overlay.querySelector(".ra-lightbox-close");

  function openLightbox(image) {
    fullImage.src = image.src;
    fullImage.alt = image.alt || "";
    caption.textContent = image.alt || "";
    overlay.classList.add("is-open");
    document.body.classList.add("ra-lightbox-open");
  }

  function closeLightbox() {
    overlay.classList.remove("is-open");
    document.body.classList.remove("ra-lightbox-open");
    fullImage.src = "";
  }

  images.forEach((image) => {
    image.addEventListener("click", () => openLightbox(image));
  });

  closeButton.addEventListener("click", closeLightbox);

  overlay.addEventListener("click", (event) => {
    if (event.target === overlay) {
      closeLightbox();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeLightbox();
    }
  });
});
