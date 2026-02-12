import { schoolList } from "./schools.js";

const input = document.getElementById("schoolInput");
const results = document.getElementById("results");

input.addEventListener("input", () => {
  const query = input.value.toLowerCase();
  results.innerHTML = "";

  if (!query) return;

  const matches = schoolList
    .filter(s => s.toLowerCase().includes(query))
    .slice(0, 10);

  matches.forEach(match => {
    const div = document.createElement("div");
    div.textContent = match;
    div.onclick = () => {
      input.value = match;
      results.innerHTML = "";
      localStorage.setItem("nervarah_school", match);
    };
    results.appendChild(div);
        <!-- your page content above -->

    <script type="module" src="/js/autocomplete.js"></script>
</body>
</html>

  });
});
