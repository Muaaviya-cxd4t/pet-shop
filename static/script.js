document.querySelectorAll(".filter").forEach(button => {
  button.addEventListener("click", () => {
    document.querySelector(".filter.active")?.classList.remove("active");
    button.classList.add("active");
    const category = button.dataset.filter;
    document.querySelectorAll(".product-card").forEach(card => {
      card.style.display = category === "All" || card.dataset.category === category ? "" : "none";
    });
  });
});
document.querySelectorAll(".qty-form").forEach(form => {
  const input = form.querySelector('input[name="quantity"]');
  form.querySelector(".minus").addEventListener("click", () => {
    input.value = Math.max(0, Number(input.value) - 1);
    form.requestSubmit();
  });
  form.querySelector(".plus").addEventListener("click", () => {
    input.value = Math.min(20, Number(input.value) + 1);
    form.requestSubmit();
  });
});
document.querySelectorAll(".flash").forEach(el => setTimeout(() => el.remove(), 3500));
