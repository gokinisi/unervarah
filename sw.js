// sw.js - Service Worker for web push

self.addEventListener('push', event => {
  const data = event.data.json();
  const options = {
    body: data.body || 'Your daily motivation has arrived!',
    icon: '/icon.png',  // optional - add a 192x192 PNG later
    badge: '/badge.png' // optional
  };
  event.waitUntil(
    self.registration.showNotification(data.title || 'Nervarah', options)
  );
});

self.addEventListener('notificationclick', event => {
  event.notification.close();
  event.waitUntil(
    clients.openWindow('http://localhost:5000')  // or your deployed URL later
  );
});