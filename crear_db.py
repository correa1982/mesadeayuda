import sqlite3

SCHEMA_USERS = '''
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  display_name TEXT NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL CHECK(role IN ('admin','usuario')),
  created_at TEXT NOT NULL,
  firma_img TEXT
);
'''

SCHEMA_TICKETS = '''
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_by INTEGER NOT NULL,
    created_at TEXT NOT NULL,
    fecha_inicio TEXT, fecha_final TEXT, hora_inicio TEXT, hora_final TEXT,
    sede TEXT, ubicacion TEXT,
    soporte_hardware INTEGER DEFAULT 0,
    soporte_Software INTEGER DEFAULT 0,
    soporte_redes INTEGER DEFAULT 0,
    equipo_equipo TEXT, equipo_marca TEXT, equipo_modelo TEXT, equipo_cod_inventario TEXT,
    equipo_coin TEXT, equipo_disco TEXT, equipo_ram TEXT, equipo_procesador TEXT,
    servicio_tipo TEXT, servicio_otro TEXT, falla_asociada TEXT,
    descripcion_solicitud TEXT, descripcion_trabajo TEXT,
    eval_calidad_servicio INTEGER, eval_calidad_informacion INTEGER,
    eval_oportunidad_respuesta INTEGER, eval_actitud_tecnico INTEGER,
    firma_usuario_gestiona_img TEXT, firma_tecnico_mantenimiento_img TEXT,
    firma_logistica_img TEXT, firma_supervisor_img TEXT,
    firma_usuario_gestiona_nombre TEXT, firma_tecnico_mantenimiento_nombre TEXT,
    firma_logistica_nombre TEXT, firma_supervisor_nombre TEXT,
    estado TEXT,
    finalizado_at TEXT,
    FOREIGN KEY(created_by) REFERENCES users(id)
);
'''

def main():
    db = sqlite3.connect('mesa_ayuda/instance/ticket_app.db')
    db.executescript(SCHEMA_USERS)
    db.executescript(SCHEMA_TICKETS)
    db.commit()
    print('Base de datos y tablas creadas correctamente.')

if __name__ == '__main__':
    main()
