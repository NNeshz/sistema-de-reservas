import { Instagram, BookAIcon, BookOpenIcon, PercentIcon, Users2Icon, Clock } from "lucide-react";

export const landingPageData = [
    {
      name: "Redes Sociales",
      className: "col-span-3 lg:col-span-1",
      background:
        "https://images.unsplash.com/photo-1589270018935-ae7e307e79b6?q=80&w=1688&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      Icon: Instagram,
      description: "No te pierdas ninguna de nuestras actualizaciones.",
      href: "/",
      cta: "Conoce más",
    },
    {
      name: "Blog",
      className: "col-span-3 lg:col-span-2",
      Icon: BookAIcon,
      background:
        "https://images.unsplash.com/photo-1545239351-ef35f43d514b?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      description: "Descubre los mejores consejos para tu salud y bienestar.",
      href: "/",
      cta: "Leer más",
    },
    {
      name: "Menu",
      description:
        "Conoce nuestra carta y descubre los platillos que tenemos para ti.",
      href: "/",
      cta: "Ver menú",
      Icon: BookOpenIcon,
      className: "col-span-3 lg:col-span-2",
      background:
        "https://images.unsplash.com/photo-1568031813264-d394c5d474b9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bWVudXxlbnwwfHwwfHx8MA%3D%3D",
    },
    {
      name: "Promociones",
      description: "Descubre nuestras promociones y descuentos.",
      href: "/",
      cta: "Ver promociones",
      Icon: PercentIcon,
      className: "col-span-3 lg:col-span-1",
      background:
        "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGZvb2R8ZW58MHx8MHx8fDA%3D",
    },
    {
      name: "Nosotros",
      description: "Conoce más sobre nosotros y nuestro equipo.",
      href: "/",
      cta: "Conoce más",
      Icon: Users2Icon,
      className: "col-span-3 lg:col-span-1",
      background:
        "https://images.unsplash.com/photo-1543269865-cbf427effbad?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    {
      name: "Reservaciones",
      description: "Reserva tu mesa y disfruta de una experiencia única.",
      href: "/",
      cta: "Reservar",
      Icon: Clock,
      className: "col-span-3 lg:col-span-2",
      background:
        "https://images.unsplash.com/photo-1634234498573-29224acf2907?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cmVzZXJ2YXRpb258ZW58MHx8MHx8fDA%3D",
    },
  ];

export const topDishesData = [
  {
    name: "Camarones en Habanero",
    description: "Camarones al ajillo con salsa de habanero.",
    imgSource: "https://images.unsplash.com/photo-1625943553852-781c6dd46faa?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8cGxhdGlsbG8lMjBkZSUyMGNhbWFyb25lc3xlbnwwfHwwfHx8MA%3D%3D",
    price: 200,
    stars: 4.5,
  },
  {
    name: "Carne Asada",
    description: "Carne asada con guacamole y tortillas de maíz.",
    imgSource: "https://images.unsplash.com/photo-1625937329935-287441889bce?q=80&w=2080&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    price: 150,
    stars: 4.5,
  },
  {
    name: "Spaghetti Carbonara",
    description: "Spaghetti con salsa carbonara y queso parmesano.",
    imgSource: "https://images.unsplash.com/photo-1685156329688-ffe9c1a99a06?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    price: 100,
    stars: 4.7
  }
]