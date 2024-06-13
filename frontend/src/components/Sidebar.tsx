"use client";

import { useState } from "react";
import Link from "next/link";
import { Apple, MenuIcon, Percent, User, Users2 } from "lucide-react";
import { ModeToggle } from "./ModeToggle";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import Image from "next/image";

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="flex flex-col h-[98vh] w-52 p-5 m-2 rounded-lg bg-yellow-500 shadow-2xl justify-between">
      <div>
        <div className="mb-12">
          <Link
            href="/"
            className="font-bold text-xl flex gap-2 items-center hover:cursor-pointer"
          >
            <Image
              src={"/olla-caliente.png"}
              alt="Logo de la empresa"
              width={35}
              height={35}
            />{" "}
            <p className="text-2xl">FastFood</p>
          </Link>
        </div>
        <nav className="flex flex-col gap-y-4">
          <Link
            href="/menu"
            className="text-lg flex gap-2 items-center hover:cursor-pointer"
          >
            <MenuIcon className="w-5 h-5 text-yellow-700" /> <p className="font-semibold">MENU</p>
          </Link>
          <Link
            href="/promociones"
            className="text-lg flex gap-2 items-center hover:cursor-pointer"
          >
            <Percent className="w-5 h-5 text-yellow-700" /> <p className="font-semibold">PROMOS</p>
          </Link>
          <Link
            href="/nosotros"
            className="text-lg flex gap-2 items-center hover:cursor-pointer"
          >
            <Users2 className="w-5 h-5 text-yellow-700" /> <p className="font-semibold">NOSOTROS</p>
          </Link>
        </nav>
      </div>

      <div className="flex flex-col gap-2">
        {/* Ver si podemos implementar el modo noche o solo no queda */}
        {/* <ModeToggle /> */}
        <DropdownMenu>
          <DropdownMenuTrigger className="flex items-center w-full py-2 pl-2 gap-2 rounded-md justify-center">
            <User className="w-5 h-5 text-yellow-700" />
            Tu cuenta
          </DropdownMenuTrigger>
          <DropdownMenuContent>
            <DropdownMenuLabel>Mi cuenta</DropdownMenuLabel>
            <DropdownMenuSeparator />
            <DropdownMenuItem>Perfil</DropdownMenuItem>
            <DropdownMenuItem>Notificaciones</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
    </div>
  );
};

export default Sidebar;
