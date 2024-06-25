import SignIn from "@/components/SignIn";
import SignUp from "@/components/SignUp";
import MaxWidthWrapper from "@/components/shared/MaxWidthWrapper";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";

const TabsDemo = () => {
  return (
    <div className="w-full h-screen px-5">
      <MaxWidthWrapper className="h-full flex items-center justify-center">
        <Tabs defaultValue="account" className="w-[400px]">
          <TabsList className="grid w-full grid-cols-2">
            <TabsTrigger value="signin">Sign in</TabsTrigger>
            <TabsTrigger value="signup">Sign up</TabsTrigger>
          </TabsList>
          <TabsContent value="signin">
            <SignIn />
          </TabsContent>
          <TabsContent value="signup">
            <SignUp />
          </TabsContent>
        </Tabs>
      </MaxWidthWrapper>
    </div>
  );
};

export default TabsDemo;
