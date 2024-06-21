import Link from "next/link";
import Image from "next/image";
import MaxWidthWrapper from "./MaxWidthWrapper";
import LogoOlla from "../../public/olla-caliente.png";
import isUserAuth from "@/lib/server";

const Navbar = () => {
  let isLogged = isUserAuth();

  return (
    <div className="relative flex h-[6.5vh] w-full bg-yellow-400 shadow-xl justify-between">
      <MaxWidthWrapper className="flex items-center justify-between w-full px-4">
        <Link href="/" className="flex items-center space-x-2">
          <Image src={LogoOlla} alt="Logo" width={40} height={40} />
          <p className="font-bold text-2xl">FastFood</p>
        </Link>
        <nav className="hidden md:flex space-x-8 items-center">
          <Link href="/menu" className="text-base font-semibold">
            MENU
          </Link>
          {isLogged ? (
            <Link href="/profile" className="text-base font-semibold">
              PERFIL
            </Link>
          ) : (
            <Link href="/signin" className="text-base font-semibold">
              UNETE
            </Link>
          )}
        </nav>
      </MaxWidthWrapper>  
    </div>      
  );
};

export default Navbar;
