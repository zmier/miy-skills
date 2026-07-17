(function () {
  "use strict";

  const data = window.TIMELINE_EX_DATA;
  if (!data) return;

  const nodesById = new Map(data.nodes.map((node) => [node.id, node]));
  const typeLabels = { event: "EVT", obligation: "OBL", gate: "GATE", outcome: "OUT" };
  let timeline = null;
  let items = null;

  const escapeHtml = (value) =>
    String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");

  const listHtml = (values, fallback) =>
    values && values.length
      ? `<ul>${values.map((value) => `<li>${escapeHtml(value)}</li>`).join("")}</ul>`
      : `<p>${escapeHtml(fallback)}</p>`;

  function makeItem(node) {
    const hasRange = Boolean(node.end);
    return {
      id: node.id,
      group: node.group,
      start: node.start,
      end: node.end,
      type: hasRange ? "range" : "box",
      className: `item item--${node.type} item--${node.certainty}`,
      content: `<div class="item-content"><strong>${escapeHtml(node.shortTitle)}</strong></div>`,
      title: `${escapeHtml(node.title)} · ${escapeHtml(node.displayTime)}`,
    };
  }

  function renderMeta() {
    document.title = data.meta.title;
    document.getElementById("project-title").textContent = data.meta.title;
    document.getElementById("project-subtitle").textContent = data.meta.subtitle;
    document.getElementById("updated-at").textContent = `数据更新于 ${data.meta.updatedAt}`;
    document.getElementById("timeline-note").textContent = data.meta.visualizationWindowNote;
    document.getElementById("summary-grid").innerHTML = data.meta.summaryCards
      .map(
        (card) => `<article class="summary-card ${card.tone ? `summary-card--${escapeHtml(card.tone)}` : ""}">
          <span>${escapeHtml(card.label)}</span><strong>${escapeHtml(card.value)}</strong><small>${escapeHtml(card.note)}</small>
        </article>`,
      )
      .join("");
  }

  function renderRoute() {
    const parts = [];
    data.meta.mainRoute.forEach((id, index) => {
      const node = nodesById.get(id);
      if (!node) return;
      parts.push(`<button class="route-node route-node--${node.type}" data-node-id="${escapeHtml(id)}" type="button">
        <span>${typeLabels[node.type]}</span><strong>${escapeHtml(node.shortTitle)}</strong><time>${escapeHtml(node.displayTime)}</time>
      </button>`);
      const nextId = data.meta.mainRoute[index + 1];
      if (nextId) {
        const link = data.links.find((candidate) => candidate.from === id && candidate.to === nextId);
        parts.push(`<div class="route-arrow"><span>${escapeHtml(link?.label || "进入下一状态")}</span><b>→</b></div>`);
      }
    });
    const container = document.getElementById("route-chain");
    container.innerHTML = parts.join("");
    container.querySelectorAll("[data-node-id]").forEach((button) =>
      button.addEventListener("click", () => openDrawer(button.dataset.nodeId)),
    );
  }

  function renderTable() {
    const body = document.getElementById("node-table");
    body.innerHTML = data.nodes
      .map(
        (node) => `<tr tabindex="0" data-node-id="${escapeHtml(node.id)}">
          <td><strong>${escapeHtml(node.title)}</strong><small>${escapeHtml(node.id)}</small></td>
          <td>${escapeHtml(node.displayTime)}</td>
          <td><span class="status status--${escapeHtml(node.status)}">${escapeHtml(node.statusLabel)}</span></td>
          <td>${escapeHtml(node.prerequisites[0] || "由来源事件创建")}</td>
          <td>${escapeHtml(node.affectedTasks.join("、"))}</td>
        </tr>`,
      )
      .join("");
    body.querySelectorAll("[data-node-id]").forEach((row) => {
      row.addEventListener("click", () => openDrawer(row.dataset.nodeId));
      row.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") openDrawer(row.dataset.nodeId);
      });
    });
  }

  function initializeTimeline() {
    const status = document.getElementById("timeline-status");
    if (!window.vis?.Timeline || !window.vis?.DataSet) {
      status.hidden = false;
      status.textContent = "交互式时间轴未加载；生命周期链、节点清单和 Markdown 档案仍可使用。";
      return;
    }

    items = new window.vis.DataSet(data.nodes.map(makeItem));
    const groups = new window.vis.DataSet(
      data.groups.map((group) => ({
        id: group.id,
        order: group.order,
        content: `<div class="group-label"><strong>${escapeHtml(group.label)}</strong><span>${escapeHtml(group.code)}</span></div>`,
      })),
    );
    const options = {
      start: data.meta.initialWindow.start,
      end: data.meta.initialWindow.end,
      min: data.meta.minDate,
      max: data.meta.maxDate,
      height: "470px",
      stack: true,
      showCurrentTime: true,
      horizontalScroll: true,
      verticalScroll: true,
      zoomKey: "ctrlKey",
      groupOrder: "order",
      margin: { item: 15, axis: 20 },
      orientation: { axis: "bottom", item: "top" },
      selectable: true,
    };
    timeline = new window.vis.Timeline(document.getElementById("timeline"), items, groups, options);
    timeline.on("select", ({ items: selected }) => selected[0] && openDrawer(selected[0]));
  }

  function openDrawer(id) {
    const node = nodesById.get(id);
    if (!node) return;
    document.getElementById("drawer-content").innerHTML = `
      <header class="drawer-header"><span class="type">${typeLabels[node.type]}</span><h2>${escapeHtml(node.title)}</h2><code>${escapeHtml(node.id)}</code></header>
      <p class="drawer-summary">${escapeHtml(node.summary)}</p>
      <dl><dt>时间</dt><dd>${escapeHtml(node.displayTime)}</dd><dt>状态</dt><dd>${escapeHtml(node.statusLabel)}</dd><dt>权威方</dt><dd>${escapeHtml(node.authority)}</dd><dt>来源</dt><dd>${escapeHtml(node.source)}</dd></dl>
      <section><h3>前置条件</h3>${listHtml(node.prerequisites, "无额外前置条件。")}</section>
      <section><h3>影响 TASK</h3>${listHtml(node.affectedTasks, "尚未映射。")}</section>
      ${node.passUnlocks ? `<section><h3>通过后解锁</h3><p>${escapeHtml(node.passUnlocks)}</p></section>` : ""}
      ${node.failureEffect ? `<section><h3>失败影响</h3><p>${escapeHtml(node.failureEffect)}</p></section>` : ""}
      <section><h3>当前下一步</h3><p>${escapeHtml(node.nextAction)}</p></section>
      <a class="document-link" href="${encodeURI(node.document)}" target="_blank" rel="noreferrer">打开节点档案 ↗</a>`;
    document.getElementById("drawer-backdrop").hidden = false;
    document.getElementById("drawer").classList.add("is-open");
    document.getElementById("drawer").setAttribute("aria-hidden", "false");
  }

  function closeDrawer() {
    document.getElementById("drawer-backdrop").hidden = true;
    document.getElementById("drawer").classList.remove("is-open");
    document.getElementById("drawer").setAttribute("aria-hidden", "true");
    if (timeline) timeline.setSelection([]);
  }

  function bindControls() {
    document.querySelectorAll("[data-filter]").forEach((button) =>
      button.addEventListener("click", () => {
        document.querySelectorAll("[data-filter]").forEach((item) => item.classList.remove("is-active"));
        button.classList.add("is-active");
        if (!items) return;
        const filtered = button.dataset.filter === "all"
          ? data.nodes
          : data.nodes.filter((node) => node.type === button.dataset.filter);
        items.clear();
        items.add(filtered.map(makeItem));
      }),
    );
    document.getElementById("fit-all").addEventListener("click", () => timeline?.fit({ animation: true }));
    document.getElementById("go-today").addEventListener("click", () => timeline?.moveTo(new Date(), { animation: true }));
    document.getElementById("drawer-close").addEventListener("click", closeDrawer);
    document.getElementById("drawer-backdrop").addEventListener("click", closeDrawer);
    document.addEventListener("keydown", (event) => event.key === "Escape" && closeDrawer());
  }

  renderMeta();
  renderRoute();
  renderTable();
  initializeTimeline();
  bindControls();
})();
