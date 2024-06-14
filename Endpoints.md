# Tables

- GET /tables/ - Listar todas las mesas.
- POST /tables/ - Crear una nueva mesa.
- GET /tables/{id}/ - Obtener detalles de una mesa específica.
- PUT /tables/{id}/ - Actualizar una mesa específica.
- PATCH /tables/{id}/ - Actualizar parcialmente una mesa específica.
- DELETE /tables/{id}/ - Eliminar una mesa específica.

# Reservation States

- GET /reservation-states/ - Listar todos los estados de reservación.
- POST /reservation-states/ - Crear un nuevo estado de reservación.
- GET /reservation-states/{id}/ - Obtener detalles de un estado de reservación específico.
- PUT /reservation-states/{id}/ - Actualizar un estado de reservación específico.
- PATCH /reservation-states/{id}/ - Actualizar parcialmente un estado de reservación específico.
- DELETE /reservation-states/{id}/ - Eliminar un estado de reservación específico.

# Menus

- GET /menus/ - Listar todos los menús.
- POST /menus/ - Crear un nuevo menú.
- GET /menus/{id}/ - Obtener detalles de un menú específico.
- PUT /menus/{id}/ - Actualizar un menú específico.
- PATCH /menus/{id}/ - Actualizar parcialmente un menú específico.
- DELETE /menus/{id}/ - Eliminar un menú específico.

# Reservations

- GET /reservations/ - Listar todas las reservaciones.
- POST /reservations/ - Crear una nueva reservación.
- GET /reservations/{id}/ - Obtener detalles de una reservación específica.
- PUT /reservations/{id}/ - Actualizar una reservación específica.
- PATCH /reservations/{id}/ - Actualizar parcialmente una reservación específica.
- DELETE /reservations/{id}/ - Eliminar una reservación específica.

# Reservation Menus

- GET /reservation-menus/ - Listar todos los menús de reservación.
- POST /reservation-menus/ - Crear un nuevo menú de reservación.
- GET /reservation-menus/{id}/ - Obtener detalles de un menú de reservación específico.
- PUT /reservation-menus/{id}/ - Actualizar un menú de reservación específico.
- PATCH /reservation-menus/{id}/ - Actualizar parcialmente un menú de reservación específico.
- DELETE /reservation-menus/{id}/ - Eliminar un menú de reservación específico.

# Staff Only

## GET /staff-only/ - Vista restringida solo para el personal autorizado.

### User Management / Authentication Endpoints

- POST /user/create/ - Crear un nuevo usuario.
- POST /user/login/ - Iniciar sesión y obtener un token.
- POST /user/token/verify/ - Verificar la validez de un token.
- POST /user/token/refresh/ - Obtener un nuevo token de acceso mediante el refresh token.
- GET /user/detail/ - Obtener detalles de un usuario.

### User Management / Update User

- PUT /user/update/ - Actualizar un usuario.

### User Management / Delete User

- DELETE /user/delete/ - Eliminar un usuario.

### User Management / Logout

- POST /user/logout/ - Cerrar sesión (requiere refresh token).

# Invitation Processing

- GET /invite/{uuid:token}/ - Procesar una invitación utilizando un token único.

Email Handling

- GET /email-form/ - Mostrar un formulario para enviar correos.
- POST /send/ - Enviar un correo utilizando la información proporcionada en el formulario.