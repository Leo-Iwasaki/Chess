//
//  ContentView.swift
//  Chess
//
//  Created by Kaede Sugano on 19/12/2023.
//

import SwiftUI

let screenWidth = UIScreen.main.bounds.width
let screenHeight = UIScreen.main.bounds.height
let rows = 8
let columns = 8

enum ChessSide {
    case white, black
}

struct ContentView: View {
    @State private var scrollViewTexts: [String] = []
    @StateObject var viewModel = ChessboardViewModel()
    
    var body: some View {
        
        NavigationView {
            VStack {
                ScrollViewReader { scrollViewProxy in
                    ScrollView(.horizontal, showsIndicators: false) {
                        HStack {
                            ForEach(scrollViewTexts.indices, id: \.self) { index in
                                Text(scrollViewTexts[index])
                                    .foregroundColor(Color("historybartxt"))
                                    .padding(.horizontal, 8)
                                    .id(index)
                            }
                        }
                        .onChange(of: scrollViewTexts) { _ in
                            if let last = scrollViewTexts.indices.last {
                                scrollViewProxy.scrollTo(last, anchor: .trailing)
                            }
                        }
                    }
                    .background(Color("historybar"))
                    .frame(height: screenHeight * 0.02)
                }
                
                Spacer()
                
                ChessboardView(side: .black, viewModel: viewModel) { piece in
                    let index = ChessboardHelper.indexForButton(piece: piece)
                    self.scrollViewTexts.append("\(ChessboardHelper.columnLetter(from: index.row))\(index.column + 1)")
                }
                
                Spacer()
            }
            .background(Color("background"))
            .navigationBarTitle("Chess", displayMode: .inline)
            .navigationBarColor(Color("navbar"))
        }
        .tabBarView()
    }
    
}

extension View {
    func navigationBarColor(_ backgroundColor: Color) -> some View {
        let uiColor = UIColor(backgroundColor)
        return self.modifier(NavigationBarModifier(backgroundColor: uiColor))
    }
}

struct NavigationBarModifier: ViewModifier {
    
    var backgroundColor: UIColor?
    var titleColor: UIColor?
    
    init(backgroundColor: UIColor?, titleColor: UIColor? = .white) {
        self.backgroundColor = backgroundColor
        self.titleColor = titleColor
        
        let coloredAppearance = UINavigationBarAppearance()
        coloredAppearance.configureWithOpaqueBackground()
        coloredAppearance.backgroundColor = backgroundColor
        coloredAppearance.titleTextAttributes = [.foregroundColor: titleColor ?? .white]
        coloredAppearance.largeTitleTextAttributes = [.foregroundColor: titleColor ?? .white]
        
        UINavigationBar.appearance().standardAppearance = coloredAppearance
        UINavigationBar.appearance().compactAppearance = coloredAppearance
        UINavigationBar.appearance().scrollEdgeAppearance = coloredAppearance
    }
    
    func body(content: Content) -> some View {
        ZStack {
            content
        }
    }
}

extension View {
    func tabBarView() -> some View {
        self.modifier(TabBarModifier())
    }
}

struct TabBarModifier: ViewModifier {
    func body(content: Content) -> some View {
        content
            .toolbar {
                ToolbarItemGroup(placement: .bottomBar) {
                    Button(action: {}) {
                        Image(systemName: "house")
                    }
                    Spacer()
                    Button(action: {}) {
                        Image(systemName: "magnifyingglass")
                    }
                    Button(action: {}) {
                        Image(systemName: "person")
                    }
                }
            }
            .background(Color("navbar"))
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
