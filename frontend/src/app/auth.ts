export const signIn = async ({
  username,
  password,
}: {
  username: string;
  password: string;
}) => {
  console.log(`Signing in as ${username} with password ${password}`);
};
