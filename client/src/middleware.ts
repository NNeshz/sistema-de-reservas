import type { NextRequest } from "next/server";
import { NextResponse } from "next/server";

export function middleware(request: NextRequest) {
  const currentUser = request.cookies.get("jwt")?.value;

  if(!currentUser && request.nextUrl.pathname.startsWith("/profile")) {
    return NextResponse.rewrite(new URL("/auth", request.url))
  }

  if(currentUser && request.nextUrl.pathname.startsWith("/auth")) {
    return NextResponse.rewrite(new URL("/", request.url))
  }
}

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|.*\\.png$).*)"],
};
