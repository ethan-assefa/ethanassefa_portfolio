document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.collapsible').forEach(function(item) {
    const summary = item.querySelector('.summary');
    const details = item.querySelector('.details');
    if (!summary || !details) return;
    summary.addEventListener('click', function() {
      item.classList.toggle('expanded');
    });
  });
});