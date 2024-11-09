# ¿Qué es Server-Side Rendering?

SSR, o renderizado del lado del servidor, implica que cuando un usuario solicita una página web, el servidor genera el contenido completo (HTML, CSS y JavaScript) y lo envía al navegador. Esto contrasta con el **Client-Side Rendering (CSR)**, donde el navegador debe ejecutar JavaScript para construir la página después de recibir una estructura básica.

## Funcionamiento de SSR

1. **Solicitud Inicial**: Cuando un usuario visita un sitio web por primera vez, el navegador envía una solicitud al servidor.
2. **Generación de Contenido**: El servidor procesa esta solicitud y genera la página HTML completa, incluyendo cualquier contenido dinámico que pueda ser necesario.
3. **Envío al Navegador**: El servidor envía este HTML al navegador, que lo renderiza inmediatamente.
4. **Interactividad Posterior**: Una vez que el HTML está cargado, se pueden realizar peticiones adicionales para obtener datos dinámicos (usualmente en formato JSON), permitiendo que la aplicación siga siendo interactiva sin necesidad de recargar la página.

## Ventajas de SSR

- **Mejora del SEO**: Al enviar contenido HTML completo, los motores de búsqueda pueden indexar mejor las páginas, lo que mejora la visibilidad del sitio.
- **Carga Inicial Rápida**: Los usuarios ven contenido más rápidamente porque no necesitan esperar a que se ejecute JavaScript para renderizar la página.
- **Accesibilidad**: Las páginas generadas son accesibles incluso si JavaScript está deshabilitado en el navegador del usuario.

## Desventajas de SSR

- **Carga del Servidor**: SSR puede aumentar la carga en el servidor, ya que cada solicitud requiere que el servidor genere HTML dinámicamente.
- **Menor Interactividad Inicial**: Aunque la carga inicial es rápida, las interacciones posteriores pueden ser más lentas si requieren múltiples solicitudes al servidor.
