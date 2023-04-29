import Image from "next/image";
import { Drawer } from "flowbite";
import type { DrawerOptions, DrawerInterface } from "flowbite";
import { useEffect, useState } from "react";

export default function CardPostContent() {
  const [drawer, setDrawer] = useState<any>(null);

  useEffect(() => {
    const target = document.getElementById('drawer-post');
    const options: DrawerOptions = {
      placement: 'left',
      backdrop: true,
      bodyScrolling: false,
      edge: false,
      edgeOffset: '',
      backdropClasses: 'bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-30',
      onHide: () => {
        console.log('drawer is hidden');
      },
      onShow: () => {
        console.log('drawer is shown');
      },
      onToggle: () => {}
    }

    const drawer: DrawerInterface = new Drawer(target, options);
    setDrawer(drawer);
  }, []);

  return (
    <div className="shadow-sm bg-white overflow-hidden rounded-md">
      <div className="px-4 py-3 flex items-center gap-3">
        <div className="flex justify-center items-center w-10 h-10 rounded-full border bg-gray-200">
          <Image src={"/icons/person.svg"} width={24} height={24} alt="person" />
        </div>
        <div className="flex-1">
          <button
            className="w-full h-9 bg-blue-700 rounded-md"
            type="button" onClick={() => drawer.show()}
            data-drawer-target="drawer-post"
            aria-controls="drawer-post"
          >
            <span className="text-white text-sm">Buat Postingan</span>
          </button>
        </div>
      </div>
      <div id="drawer-post" className="fixed top-0 left-0 z-40 h-screen p-4 overflow-y-auto transition-transform -translate-x-full bg-white w-80 dark:bg-gray-800" tabIndex={1}>
        <h5 id="drawer-label" className="inline-flex items-center mb-3 text-base font-semibold text-gray-500 dark:text-gray-400">Buat Postingan</h5>
        <button
          type="button"
          data-drawer-hide="drawer-post"
          aria-controls="drawer-post"
          className="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 absolute top-2.5 right-2.5 inline-flex items-center"
          onClick={() => drawer.hide()}
        >
          <Image src={"/icons/x.svg"} width={18} height={18} alt="" />
        </button>
        <div className="border-t">
          <form action="#" className="mt-4">
            <div className="mb-6">
              <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
              <input type="email" id="email" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@company.com" />
            </div>
            <div className="mb-6">
              <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Subject</label>
              <input type="text" id="subject" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Let us know how we can help you" />
            </div>
            <div className="mb-6">
              <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your message</label>
              <textarea id="message" rows={4} className="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Your message..."></textarea>
            </div>
            <button type="submit" className="text-white bg-blue-700 hover:bg-blue-800 w-full focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800 block">Send message</button>
          </form>
        </div>
      </div>
    </div>
  )
}