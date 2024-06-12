"use client";

import { useState } from "react";
import Link from "next/link";
import { Apple, MenuIcon, Percent, User } from "lucide-react";
import { ModeToggle } from "./ModeToggle";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

const Sidebar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="flex flex-col h-[98vh] w-52 p-5 m-2 rounded-lg border shadow-2xl justify-between">
      <div>
        <div className="mb-12">
          <Link href="/" className="font-bold text-xl flex gap-2 items-center hover:cursor-pointer">
            <Apple className="w-6 h-6" /> <p className="text-yellow-500">FastFood</p>
          </Link>
        </div>
        <nav className="flex flex-col gap-y-4">
          <Link
            href="/menu"
            className="text-lg flex gap-2 items-center hover:cursor-pointer"
          >
            <MenuIcon className="w-5 h-5 text-yellow-500" /> Menú
          </Link>
          <Link
            href="/promociones"
            className="text-lg flex gap-2 items-center hover:cursor-pointer"
          >
            <Percent className="w-5 h-5 text-yellow-500" /> Promociones
          </Link>
        </nav>
      </div>

      <div className="flex flex-col gap-2">
        <ModeToggle />
        <DropdownMenu>
          <DropdownMenuTrigger className="flex items-center border w-full py-2 pl-2 gap-2 rounded-md justify-center">
            <User className="w-5 h-5 text-yellow-500" />
            User
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
